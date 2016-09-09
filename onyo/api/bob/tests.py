# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from models import Address

from api import settings
from api import utils


class Mock():

    def __init__(self):
        self.address = {
            'country': 'brasil',
            'state': 'rio de janeiro',
            'city': 'niteroi'
        }


class AddressTests(APITestCase):

    """
    Testing viewset default methods
        http://www.django-rest-framework.org/api-guide/viewsets/

                list(self, request)
                create(self, request)
                retrieve(self, request, pk=None)
                update(self, request, pk=None)
                partial_update(self, request, pk=None)
                destroy(self, request, pk=None)

    """
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.mock = Mock()
        cls.endpoint = 'address/'
        cls.endpoint_path = utils.format_url(settings.EXTERNAL_URLS['bob'], cls.endpoint)

    def setUp(self):
        response = self.client.post(
            self.endpoint_path, self.mock.address, format='json')
        self.address = response.json()

    def test_list_address(self):
        response = self.client.get(
            utils.format_url(self.endpoint_path, str(self.address['id'])), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        response = self.client.post(
            utils.format_url(self.endpoint_path), self.mock.address, format='json')
        self.address = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_address(self):
        response = self.client.get(
            utils.format_url(self.endpoint_path, str(self.address['id'])), format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

    def test_update_address(self):
        response = self.client.put(
            utils.format_url(self.endpoint_path, str(self.address['id'])), self.mock.address, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

    def test_partial_update_address(self):
        response = self.client.put(
            utils.format_url(self.endpoint_path, str(self.address['id'])), self.mock.address, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

    def test_destroy_address(self):
        response = self.client.delete(
            utils.format_url(self.endpoint_path, str(self.address['id'])), self.mock.address, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT)