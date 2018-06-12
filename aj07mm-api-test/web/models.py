# -*- coding: utf-8 -*-
from mongoengine import (
    Document,
    StringField,
    FloatField,
    IntField,
    BooleanField,
    ObjectIdField,
)


class Recipe(Document):
    name = StringField(required=True, max_length=200)
    prep_time = FloatField(required=True)
    difficulty = IntField(required=True, min_value=1, max_value=3)
    vegetarian = BooleanField(required=True)

    def rate(self, points):
        rate = Rate(self.id, points)
        return rate.save()


class Rate(Document):
    recipe_id = ObjectIdField(required=True)
    points = IntField(min_value=1, max_value=3)


class User(Document):
    username = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
