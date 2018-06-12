# -*- coding: utf-8 -*-
import unittest
import json
import settings
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse
from werkzeug import Headers

from factories import RecipeFactory
from web.models import Recipe, Rate
from web.api import create_app
from web.constants import HTTP_STATUS_CODE


class RecipeTestCase(unittest.TestCase):
    """Test case for the client methods."""

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        app = create_app(
            mongo_host=settings.MONGO_HOST,
            mongo_port=settings.MONGO_PORT,
            database=settings.DATABASE['test'],
        )
        cls.client = Client(app, BaseResponse)
        response = cls.client.post('/auth/', data=json.dumps({
            'username': 'admin',
            'password': '123',

        }), content_type='application/json')
        access_token = json.loads(response.data.decode())['access_token']
        cls.headers = Headers(['AUTHORIZATION', 'Bearer ' + access_token])

    def setUp(self):
        self.recipe = RecipeFactory.create(
            name='asdasdas',
            prep_time=3,
            difficulty=1,
            vegetarian=True,
        )

    def tearDown(self):
        Recipe.objects().delete()
        Rate.objects().delete()

    def test_list(self):
        response = self.client.get('/recipes/', headers=[self.headers])
        response_recipes = json.loads(response.data.decode())
        self.assertEqual(
            self.recipe['name'],
            response_recipes['results'][0]['name']
        )
        self.assertEqual(
            self.recipe['prep_time'],
            response_recipes['results'][0]['prep_time']
        )
        self.assertEqual(
            self.recipe['vegetarian'],
            response_recipes['results'][0]['vegetarian']
        )
        self.assertEqual(
            self.recipe['difficulty'],
            response_recipes['results'][0]['difficulty']
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])

    def test_list_with_query_parameter(self):
        self.recipe = RecipeFactory.create(
            name='asd',
            prep_time=3,
            difficulty=1,
            vegetarian=True,
        )
        response = self.client.get(
            '/recipes/?name=asd', headers=[self.headers])
        response_recipes = json.loads(response.data.decode())
        self.assertEqual(
            self.recipe['name'],
            response_recipes['results'][0]['name']
        )
        self.assertEqual(
            self.recipe['prep_time'],
            response_recipes['results'][0]['prep_time']
        )
        self.assertEqual(
            self.recipe['vegetarian'],
            response_recipes['results'][0]['vegetarian']
        )
        self.assertEqual(
            self.recipe['difficulty'],
            response_recipes['results'][0]['difficulty']
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])

    def test_create(self):
        payload = {
            'name': 'foobar',
            'prep_time': 3,
            'vegetarian': False,
            'difficulty': 1,
        }
        response = self.client.post(
            '/recipes/',
            headers=[self.headers],
            data=json.dumps(payload),
            content_type='application/json',
        )
        request_recipe = payload
        response_recipe = json.loads(response.data.decode())
        self.assertEqual(
            request_recipe['name'],
            response_recipe['name']
        )
        self.assertEqual(
            request_recipe['prep_time'],
            response_recipe['prep_time']
        )
        self.assertEqual(
            request_recipe['vegetarian'],
            response_recipe['vegetarian']
        )
        self.assertEqual(
            request_recipe['difficulty'],
            response_recipe['difficulty']
        )
        self.assertEqual(
            response.status_code,
            HTTP_STATUS_CODE['201_CREATED']
        )

    def test_create_fail(self):
        payload = {}
        response = self.client.post(
            '/recipes/',
            headers=[self.headers],
            data=json.dumps(payload),
            content_type='application/json',
        )
        response_recipe = json.loads(response.data.decode())
        self.assertEqual(
            response_recipe['error']['name'][0],
            'Missing data for required field.')
        self.assertEqual(
            response_recipe['error']['prep_time'][0],
            'Missing data for required field.'
        )
        self.assertEqual(
            response_recipe['error']['vegetarian'][0],
            'Missing data for required field.'
        )
        self.assertEqual(
            response_recipe['error']['difficulty'][0],
            'Missing data for required field.'
        )
        self.assertEqual(
            response.status_code,
            HTTP_STATUS_CODE['400_BAD_REQUEST']
        )

    def test_get(self):
        response = self.client.get(
            '/recipes/{}'.format(self.recipe.id),
            headers=[self.headers],
        )
        response_recipe = json.loads(response.data.decode())
        self.assertEqual(
            self.recipe['name'],
            response_recipe['name']
        )
        self.assertEqual(
            self.recipe['prep_time'],
            response_recipe['prep_time']
        )
        self.assertEqual(
            self.recipe['vegetarian'],
            response_recipe['vegetarian']
        )
        self.assertEqual(
            self.recipe['difficulty'],
            response_recipe['difficulty']
        )
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])

    def test_update(self):
        payload = {
            'name': 'foobar123',
            'vegetarian': True,
        }
        response = self.client.put(
            '/recipes/{}'.format(self.recipe.id),
            headers=[self.headers],
            data=json.dumps(payload),
            content_type='application/json',
        )
        response_recipe = json.loads(response.data.decode())
        self.assertEqual(payload['name'], response_recipe['name'])
        self.assertEqual(payload['vegetarian'], response_recipe['vegetarian'])
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])

    def test_delete(self):
        response = self.client.delete(
            '/recipes/{}'.format(self.recipe.id),
            headers=[self.headers],
        )
        self.assertEqual(
            response.status_code,
            HTTP_STATUS_CODE['204_NO_CONTENT']
        )

    def test_rate(self):
        payload = {
            'recipe_id': str(self.recipe.id),
            'points': 2,
        }
        response = self.client.post(
            '/recipes/{}/rating'.format(self.recipe.id),
            headers=[self.headers],
            data=json.dumps(payload),
            content_type='application/json',
        )
        rate = Rate.objects.get(recipe_id=self.recipe.id)
        self.assertEqual(2, rate.points)
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])

    def test_error_404(self):
        response = self.client.get(
            '/recipes/asdoansdoasnd'.format(self.recipe.id),
            headers=[self.headers],
        )
        self.assertEqual(
            response.status_code, HTTP_STATUS_CODE['404_NOT_FOUND'])

    def test_pagination(self):
        self.recipes = RecipeFactory.create_batch(
            size=50,
            **{
                'name': 'asdasdas',
                'prep_time': 3,
                'difficulty': 1,
                'vegetarian': True,
            }
        )
        response = self.client.get('/recipes/?page=1', headers=[self.headers])
        response_recipes = json.loads(response.data.decode())
        self.assertEqual(30, len(response_recipes['results']))
        response = self.client.get('/recipes/?page=2', headers=[self.headers])
        response_recipes = json.loads(response.data.decode())
        self.assertEqual(21, len(response_recipes['results']))
        self.assertEqual(response.status_code, HTTP_STATUS_CODE['200_OK'])
