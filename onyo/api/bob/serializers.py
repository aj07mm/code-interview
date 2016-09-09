# -*- coding: utf-8 -*-
from models import Address
from rest_framework import serializers


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = tuple(Address._meta.get_all_field_names())
