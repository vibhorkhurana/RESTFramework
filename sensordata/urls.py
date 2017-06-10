from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from django.contrib import admin
from sensordata import views as sensieview
from rest_framework.authtoken import views
"""sensorstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

urlpatterns = [
    url(r'^$',sensieview.index,name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'sensors/$',sensieview.SensorList.as_view()),
    url(r'sensors/(?P<pk>\d+)/$',sensieview.SensorDetail.as_view(),name='sensors'),
    url(r'^users/$', sensieview.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', sensieview.UserDetail.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]