from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=False)
    average_price = models.FloatField(null=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False)
    cart_uuid = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.FloatField(null=False)
    total_price = models.FloatField(null=False)