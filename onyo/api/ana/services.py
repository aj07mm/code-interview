# -*- coding: utf-8 -*-
import requests
from api import settings


class BoBService():

    """
    A API service for bob with custom methods
    """

    base_path = settings.EXTERNAL_URLS['bob']

    @staticmethod
    def post(endpoint_path, data):
        return requests.post(BoBService.base_path + endpoint_path, json=data)

    # @staticmethod
    # def put(endpoint_path, data):
    #     return requests.put(BoBService.base_path + endpoint_path, json=data)

    # @staticmethod
    # def delete(endpoint_path, data):
    #     return requests.delete(BoBService.base_path + endpoint_path, json=data)
