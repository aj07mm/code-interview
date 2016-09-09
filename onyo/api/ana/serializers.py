# -*- coding: utf-8 -*-
from models import Address
from rest_framework import serializers


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = tuple(Address._meta.get_all_field_names())
        read_only_fields = ('id',)

class AddressFormSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = tuple(Address._meta.get_all_field_names())

# class AddressFormDetailSerializer(serializers.HyperlinkedModelSerializer):

#     id = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Address
#         fields = tuple(Address._meta.get_all_field_names())
