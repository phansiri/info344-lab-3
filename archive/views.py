# Lab 1 - imports
from django.shortcuts import render, get_object_or_404, redirect
from .models import urlSites
from .forms import UrlForm
from bs4 import BeautifulSoup
import requests

# Lab 2 - imports
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Lab 3
from selenium import webdriver
from lab1.settings import STATIC_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import os, sys
import datetime
from ratelimit.decorators import ratelimit
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from archive.serializers import UrlsSerializer
from archive.serializers import UserSerializer
from django.contrib.auth.models import User
from archive.permissions import IsOwnerOrReadOnly
from django.http import Http404
from ratelimit.mixins import RatelimitMixin

# Lab 1 - url expander
@ratelimit(key='ip', rate='10/m', block='True')
@login_required(login_url='accounts/login/')
def url_list(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        urlList = urlSites.objects.all().order_by('id')
        return render(request, 'archive/url_list.html', {'urlList': urlList})

# @login_required
@ratelimit(key='ip', rate='10/m', block='True')
def url_detail(request, pk):
    urlDetail = get_object_or_404(urlSites, pk=pk)
    return render(request, 'archive/url_detail.html', {'urlDetail': urlDetail})

# @login_required
@ratelimit(key='ip', rate='10/m', block='True')
def url_new(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            source_code = requests.request('GET', post.originalUrl)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            post.finalUrl = source_code.url
            post.httpStatusCode = source_code.status_code
            post.pageTitle = soup.title.string
            # upload to s3
            # driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
            # driver.set_window_size(1024, 768)
            # driver.get(post.finalUrl)
            # name = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
            #
            # conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            # b = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
            # k = Key(b)
            # nameFile = name + '.png'
            # k.key = 'screensaver/' + nameFile
            # driver.save_screenshot('/tmp/' + nameFile)
            # k.set_contents_from_filename('/tmp/' + nameFile)
            # k.make_public()
            # os.remove('/tmp/' + nameFile)
            # post.screenShot = STATIC_URL + "screensaver/" + nameFile
            updateS3(post, 'upload')
            post.save()
            return redirect('archive.views.url_detail', pk=post.pk)
    else:
        form = UrlForm()
    return render(request, 'archive/url_edit.html', {'form': form})

# @login_required
@ratelimit(key='ip', rate='10/m', block='True')
def url_edit(request, pk):
    post = get_object_or_404(urlSites, pk=pk)
    if request.method == "POST":
        form = UrlForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            updateS3(post)
            post.save()
            return redirect('archive.views.url_detail', pk=post.pk)
    else:
        form = UrlForm(instance=post)
    return render(request, 'archive/url_edit.html', {'form': form})

# @login_required
@ratelimit(key='ip', rate='10/m', block='True')
def url_delete(request, pk):
    urlDelete = get_object_or_404(urlSites, pk=pk)
    updateS3(urlDelete, 'deletion')
    urlDelete.delete()
    return redirect('archive.views.url_list')

def updateS3(post, status):
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    driver.set_window_size(1024, 768)
    driver.get(post.finalUrl)
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    b = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
    k = Key(b)
    if status == 'upload':
        nameFile = str(post.pk) + '-' + datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.png'
        k.key = 'screensaver/' + nameFile
        driver.save_screenshot('/tmp/' + nameFile)
        k.set_contents_from_filename('/tmp/' + nameFile)
        k.make_public()
        os.remove('/tmp/' + nameFile)
        post.screenShot = STATIC_URL + "screensaver/" + nameFile
    else:
        temp = post.screenShot.split("/")
        filePath = temp[4] + '/' + temp[5]
        b.delete_key(filePath)

# Lab 3
class ApiList(RatelimitMixin, generics.ListCreateAPIView):
    ratelimit_key = 'ip'
    ratelimit_rate = '10/m'
    ratelimit_block = True
    ratelimit_method = 'GET', 'POST'

    queryset = urlSites.objects.all()
    serializer_class = UrlsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ApiDetail(RatelimitMixin, generics.RetrieveUpdateDestroyAPIView):
    ratelimit_key = 'ip'
    ratelimit_rate = '10/m'
    ratelimit_block = True
    ratelimit_method = 'GET', 'PUT', 'DELETE'

    queryset = urlSites.objects.all()
    serializer_class = UrlsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer