from django.shortcuts import render
from django.contrib.auth.models import User, Group
from models import Product, Purchase
from rest_framework import viewsets, status
from serializers import UserSerializer, GroupSerializer, ProductSerializer, PurchaseSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """

    #overwrinting method
    def update(self, request, *args, **kwargs):
        #updating attribute average_price updates all docs with the same name
        if request.data.has_key('average_price') and request.data.has_key('name'):
            Product.objects.filter(name=request.data['name']).update(average_price=request.data['average_price'])

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #create attribute average_price updates all docs with the same name
        #in case object name already exists we have to update
        if request.data.has_key('average_price') and request.data.has_key('name'):
            Product.objects.filter(name=request.data['name']).update(average_price=request.data['average_price'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Purchases to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer