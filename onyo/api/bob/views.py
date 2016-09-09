# -*- coding: utf-8 -*-
import json
import random
from models import Address
from rest_framework import viewsets
from serializers import AddressSerializer
from rest_framework.response import Response
from rest_framework import status

from django.db.models.signals import pre_save


class AddressViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request):
        address_serializer = AddressSerializer(data=request.data)

        if address_serializer.is_valid():
            address_serializer.save()

            return Response(address_serializer.data, status=status.HTTP_201_CREATED)

        return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -*- Signals -*-

def add_random_number_to_fields(sender, instance, **kwargs):
    instance.country += str(random.random())
    instance.state += str(random.random())
    instance.city += str(random.random())

pre_save.connect(add_random_number_to_fields, sender=Address)