from django.forms import widgets
from rest_framework import serializers
from archive.models import urlSites
from django.contrib.auth.models import User

class UrlsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = urlSites
        fields = ('id',
                  'owner',
                  'originalUrl',
                  'finalUrl',
                  'httpStatusCode',
                  'pageTitle',
                  'screenShot'
                  )

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.PrimaryKeyRelatedField(many=True, queryset=urlSites.objects.all())

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'urls')