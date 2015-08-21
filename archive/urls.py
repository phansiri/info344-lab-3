# Lab 1
from django.conf.urls import url, patterns
from . import views

# Lab 2
from django.contrib.auth import views as auth_views

# Lab 3
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Lab 1
    url(r'^$', views.url_list, name='url_list'),
    url(r'^url/(?P<pk>[0-9]+)/$', views.url_detail, name='url_detail'),
    url(r'^url/new/$', views.url_new, name='url_new'),
    url(r'^url/(?P<pk>[0-9]+)/edit/$', views.url_edit, name='url_edit'),
    url(r'^url/(?P<pk>[0-9]+)/delete/$', views.url_delete, name='url_delete'),

    # Lab 2
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/lab3'}),

    # Lab 3
    url(r'^api/$', views.ApiList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.ApiDetail.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/recapture/$', views.ApiDetail_Recapture.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)