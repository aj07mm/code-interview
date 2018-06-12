# -*- coding: utf-8 -*-
from marshmallow import Schema, fields, validate


class Serializer(Schema):
    pass


class RecipeSerializer(Serializer):
    id = fields.String()
    name = fields.String(
        required=True,
        validate=[validate.Length(max=200)],
    )
    prep_time = fields.Number(required=True)
    difficulty = fields.Integer(
        required=True,
        validate=[validate.Range(min=1, max=3)],
    )
    vegetarian = fields.Boolean(required=True)


class RecipeListSerializer(Serializer):
    count = fields.Integer()
    next = fields.String()
    previous = fields.String()
    results = fields.List(fields.Nested(RecipeSerializer))


class RecipeUpdateSerializer(Serializer):
    id = fields.String()
    name = fields.String(validate=[validate.Length(max=200)])
    prep_time = fields.Number()
    difficulty = fields.Integer(validate=[validate.Range(min=1, max=3)])
    vegetarian = fields.Boolean()


class RateSerializer(Serializer):
    points = fields.Integer(
        required=True,
        validate=[validate.Range(min=1, max=5)],
    )


recipe_serializer = RecipeSerializer()
recipe_list_serializer = RecipeListSerializer()
