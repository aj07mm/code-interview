# -*- coding: utf-8 -*-
import jwt
import pymongo
import hashlib
import settings
try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import (
    NotFound,
    MethodNotAllowed,
)
from marshmallow.exceptions import ValidationError as MarshmallowValidationError  # noqa
from json.decoder import JSONDecodeError
from werkzeug.wrappers import Request, Response
from mongoengine import (
    FieldDoesNotExist,
    connect,
)

from web.constants import HTTP_STATUS_CODE
from web.models import Recipe, User
from web.serializers import (
    RecipeSerializer,
    RecipeUpdateSerializer,
    RateSerializer,
    recipe_serializer,
    recipe_list_serializer,
)
from web.helpers import (
    local,
    Pagination,
    auth_protected,
    local_manager,
)


class ApiAuth(object):

    def check_auth(self, username, password):
        user = User.objects.get(username=username)
        return (
            user and
            user.password == hashlib.sha256(
                password.encode('utf-8')
            ).hexdigest()
        )

    def auth_required(self, request):
        return Response(status=HTTP_STATUS_CODE['401_UNAUTHORIZED'])


class ApiBase(ApiAuth):

    def __init__(self, config):
        self.client = pymongo.MongoClient(
            config['mongo_host'],
            config['mongo_port'],
            connect=False,
        )
        self.db = getattr(self.client, config['database'])
        connect(
            'hellofresh', host=config['mongo_host'], port=config['mongo_port'])

    def render(self, content=None, status=None):
        if content:
            return Response(
                dumps(content), status=status, mimetype='application/json'
            )
        return Response(status=status, mimetype='application/json')

    def dispatch_request(self, request):
        self.url_adapter = self.url_map.bind_to_environ(request.environ)
        local.url_adapter = self.url_adapter
        try:
            endpoint, values = self.url_adapter.match()
            return getattr(self, endpoint)(request, **values)
        except MarshmallowValidationError as e:
            return self.render({
                'error': e.messages
            }, status=HTTP_STATUS_CODE['400_BAD_REQUEST'])
        except (AttributeError, NotFound) as e:
            return self.render({
                'error': 'Path does not exists'
            }, status=HTTP_STATUS_CODE['400_BAD_REQUEST'])
        except FieldDoesNotExist as e:
            return self.render({
                'error': 'Field does not exists'
            }, status=HTTP_STATUS_CODE['400_BAD_REQUEST'])
        except MethodNotAllowed as e:
            return self.render({
                'error': 'Method not allowed'
            }, status=HTTP_STATUS_CODE['403_FORBIDDEN'])
        except JSONDecodeError as e:
            return self.render({
                'error': 'Content-Type needs to be application/json'
            }, status=HTTP_STATUS_CODE['403_FORBIDDEN'])
        except Exception as e:
            return self.render({
                'error': 'Server internal error, please contact support'
            }, status=HTTP_STATUS_CODE['400_BAD_REQUEST'])

    def wsgi_app(self, environ, start_response):
        local.request = request = Request(environ, start_response)
        response = self.dispatch_request(request)

        if response:
            return response(environ, start_response)
        return self.error_404()(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


class HelloFreshApi(ApiBase):

    url_map = Map([
        Rule('/auth', endpoint='auth', methods=['POST']),
        Rule('/', endpoint='index', methods=['GET']),
        Rule('/recipes/', endpoint='list', methods=['GET']),
        Rule('/recipes/', endpoint='create', methods=['POST']),
        Rule('/recipes/<recipe_id>', endpoint='get', methods=['GET']),
        Rule(
            '/recipes/<recipe_id>',
            endpoint='update',
            methods=['PUT', 'PATCH']
        ),
        Rule(
            '/recipes/<recipe_id>',
            endpoint='delete',
            methods=['DELETE']
        ),
        Rule(
            '/recipes/<recipe_id>/rating',
            endpoint='rating',
            methods=['POST']
        ),
    ], strict_slashes=False)

    def auth(self, request):
        data = loads(request.stream.read().decode('utf-8'))
        encoded = jwt.encode(data, 'secret', algorithm='HS256')
        return self.render({
            "access_token": encoded.decode("utf-8")
        }, status=HTTP_STATUS_CODE['200_OK'])

    def index(self, request):
        return self.render(status=HTTP_STATUS_CODE['200_OK'])

    def list(self, request):
        query_params = dict(parse_qsl(request.query_string.decode()))
        page = int(query_params.pop('page', 1))
        recipes = Recipe.objects(**query_params)
        pagination = Pagination(
            self, recipes, settings.PAGINATION_PER_PAGE, page, 'list')

        if int(pagination.page) > 1 and not pagination.results:
            raise NotFound()
        return self.render(
            recipe_list_serializer.dump(pagination).data,
            status=HTTP_STATUS_CODE['200_OK']
        )

    @auth_protected
    def create(self, request):
        data = loads(request.stream.read().decode('utf-8'))
        recipe_serialized = RecipeSerializer(strict=True).load(data)
        # save
        recipe = Recipe(**recipe_serialized.data)
        recipe.save()
        return self.render(
            recipe_serializer.dump(recipe).data,
            status=HTTP_STATUS_CODE['201_CREATED'],
        )

    def get(self, request, recipe_id):
        if (
            ObjectId.is_valid(recipe_id) and
            Recipe.objects(id=ObjectId(recipe_id))
        ):
            recipe = Recipe.objects.get(id=ObjectId(recipe_id))
            return self.render(
                recipe_serializer.dump(recipe).data,
                status=HTTP_STATUS_CODE['200_OK']
            )

    @auth_protected
    def update(self, request, recipe_id):
        if (
            ObjectId.is_valid(recipe_id) and
            Recipe.objects(id=ObjectId(recipe_id))
        ):
            data = loads(request.stream.read().decode('utf-8'))
            if data:
                recipe_serialized = RecipeUpdateSerializer(
                    strict=True).load(data)
                # update
                recipe = Recipe.objects.get(id=ObjectId(recipe_id))
                recipe.modify(**recipe_serialized.data)
                return self.render(
                    recipe_serializer.dump(recipe).data,
                    status=HTTP_STATUS_CODE['200_OK'],
                )
            return self.render({
                'error': 'payload body needs to be a non empty JSON'
            }, status=HTTP_STATUS_CODE['400_BAD_REQUEST'])

    @auth_protected
    def delete(self, request, recipe_id):
        if (
            ObjectId.is_valid(recipe_id) and
            Recipe.objects(id=ObjectId(recipe_id))
        ):
            return self.render(
                Recipe.objects(id=ObjectId(recipe_id)).delete(),
                status=HTTP_STATUS_CODE['204_NO_CONTENT'],
            )

    def rating(self, request, recipe_id):
        if (
            ObjectId.is_valid(recipe_id) and
            Recipe.objects(id=ObjectId(recipe_id))
        ):
            data = loads(request.stream.read().decode('utf-8'))
            rate_serialized = RateSerializer(strict=True).load(data)
            # update
            recipe = Recipe.objects.get(id=ObjectId(recipe_id))
            recipe.rate(rate_serialized.data['points'])
            return self.render(status=HTTP_STATUS_CODE['200_OK'])

    def error_404(self):
        return self.render(status=HTTP_STATUS_CODE['404_NOT_FOUND'])


def create_app(
    mongo_host='localhost',
    mongo_port=27017,
    database='test_database'
):
    return HelloFreshApi({
        'mongo_host': mongo_host,
        'mongo_port': mongo_port,
        'database': database,
    })


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app(
        mongo_host=settings.MONGO_HOST,
        mongo_port=settings.MONGO_PORT,
        database=settings.DATABASE['development'],
    )
    app = local_manager.make_middleware(app)
    run_simple('0.0.0.0', 8080, app, use_debugger=False, use_reloader=True)
