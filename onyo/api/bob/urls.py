# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers
from views import AddressViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)

urlpatterns = router.urls
