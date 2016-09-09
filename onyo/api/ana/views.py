# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import Address
from serializers import AddressSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from api.ana.serializers import AddressSerializer, AddressFormSerializer
from api.ana.services import BoBService
from api import utils


class AddressViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows address to be viewed or edited.

    Actions done on /bob:

        create(self, request)

    """

    endpoint = 'address/'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request):

        response = BoBService.post(self.endpoint, request.data)

        if response.status_code == status.HTTP_201_CREATED:
            response_data = response.json()

            address_serializer = AddressFormSerializer(data=response_data)
            if address_serializer.is_valid():
                address_serializer.save()

            return Response(response.json(), status=response.status_code)

        return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):

    #     response = BoBService.put(
    #         utils.format_url(self.endpoint, pk), request.data)

    #     if response.status_code == status.HTTP_200_OK:
    #         response_data = response.json()

    #         address_serializer = AddressFormDetailSerializer(data=response_data)

    #         if address_serializer.is_valid():
    #             address_serializer.save()

    #         return Response(response.json(), status=response.status_code)

    #     return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)


    # def partial_update(self, request, pk):
    #     response = BoBService.patch(
    #         utils.format_url(self.endpoint, pk), request.data)

    #     if response.status_code == status.HTTP_201_CREATED:
    #         response_data = response.json()

    #         address_serializer = AddressFormDetailSerializer(data=response_data)
    #         if address_serializer.is_valid():
    #             address_serializer.save()

    #         return Response(response.json(), status=response.status_code)

    #     return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):
    #     response = BoBService.delete(
    #         utils.format_url(self.endpoint, pk), request.data)

    #     if response.status_code == status.HTTP_204_NO_CONTENT:
    #         address = Address.objects.get(pk=pk)
    #         address.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    #     return Response(status=status.HTTP_404_NO_CONTENT)