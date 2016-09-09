# -*- coding: utf-8 -*-
from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
