from django.test import TestCase

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from gestao.models import Product, Purchase

class Mock():
	def __init__(self):
		self.product = {
			'name' : 'aosnaknsd',
			'price' : 123.0,
			'average_price' : 123.0
		}
		self.purchase = {
			'cart_uuid' : 'asdasdasd', #need to put Product!
			'quantity' : 123.0,
			'total_price' : 123.0
		}
		self.partial_product = {
			'name' : 'aosnaknsd'
		}
		self.partial_purchase = {
			'cart_uuid' : 'asdasdasd'
		}

class ProductTests(APITestCase):
	# Testing viewset default methods 
	# http://www.django-rest-framework.org/api-guide/viewsets/
		# list(self, request)
		# create(self, request)
		# retrieve(self, request, pk=None)
		# update(self, request, pk=None)
		# partial_update(self, request, pk=None)
		# destroy(self, request, pk=None)

	#status list
	# https://github.com/avinassh/status/blob/master/status.py

	### PRODUCT ###

	def test_list_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.product, format='json')
		response = self.client.get('/products/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.product, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_retrive_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.product, format='json')
		response = self.client.get('/products/' + str(response.data['id']), format='json')
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_update_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.product, format='json') #create
		response = self.client.put('/products/' + str(response.data['id']), mock.product, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_partial_update_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.partial_product, format='json') #create
		response = self.client.put('/products/' + str(response.data['id']), mock.product, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_destroy_product(self):
		mock = Mock()
		response = self.client.post('/products/', mock.partial_product, format='json') #create
		response = self.client.delete('/products/' + str(response.data['id']), mock.product, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	### PURCHASE ###

	def test_list_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.purchase, format='json')
		response = self.client.get('/purchases/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.purchase, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_retrive_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.purchase, format='json')
		response = self.client.get('/purchases/' + str(response.data['id']), format='json')
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_update_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.purchase, format='json') #create
		response = self.client.put('/purchases/' + str(response.data['id']), mock.purchase, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_partial_update_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.partial_purchase, format='json') #create
		response = self.client.put('/purchases/' + str(response.data['id']), mock.purchase, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_destroy_purchase(self):
		mock = Mock()
		response = self.client.post('/purchases/', mock.partial_purchase, format='json') #create
		response = self.client.delete('/purchases/' + str(response.data['id']), mock.purchase, format='json') #update
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)


