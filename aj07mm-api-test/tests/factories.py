# -*- coding: utf-8 -*-
import factory
from web import models


class RecipeFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = models.Recipe


class RateFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = models.Rate
