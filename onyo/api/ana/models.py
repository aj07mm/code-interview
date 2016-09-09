# -*- coding: utf-8 -*-
from django.db import models


class Address(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
