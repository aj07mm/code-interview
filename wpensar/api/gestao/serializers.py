from django.contrib.auth.models import User, Group
from models import Product, Purchase
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'average_price')

class PurchaseSerializer(serializers.ModelSerializer): #no hyperlink shit
    class Meta:
        model = Purchase
        fields = ('id', 'cart_uuid','product', 'quantity', 'total_price')