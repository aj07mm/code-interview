# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from bob import urls
from ana import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bob/', include('api.bob.urls', namespace='bob')),
    url(r'^ana/', include('api.ana.urls', namespace='ana'))
]
