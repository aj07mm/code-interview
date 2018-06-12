# -*- coding: utf-8 -*-
import unittest
import pymongo
import settings
from mongoengine import connect
from factories import RecipeFactory
from web.models import Recipe, Rate


class RecipeTestCase(unittest.TestCase):

    def set_up_database(self):
        self.client = pymongo.MongoClient(
            settings.MONGO_HOST,
            settings.MONGO_PORT,
            connect=False,
        )
        self.db = getattr(self.client, settings.DATABASE['test'])
        connect(
            'hellofresh', host=settings.MONGO_HOST, port=settings.MONGO_PORT)

    def setUp(self):
        self.set_up_database()

    def tearDown(self):
        Recipe.objects().delete()
        Rate.objects().delete()

    def test_rating_recipe(self):
        recipe = RecipeFactory.create(
            name='asdasdas',
            prep_time=3,
            difficulty=1,
            vegetarian=True,
        )
        recipe.save()
        recipe.rate(2)
        rates = Rate.objects(recipe_id=recipe.id)
        self.assertTrue(rates)
