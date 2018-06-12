# -*- coding: utf-8 -*-
import jwt
import math
from werkzeug.local import Local, LocalManager
from werkzeug.utils import cached_property

local = Local()
local_manager = LocalManager([local])


def url_for(endpoint, _external=False, **values):
    return local.url_adapter.build(endpoint, values, force_external=_external)


class Pagination(object):

    """
        GET https://api.example.org/accounts/?page=4

        HTTP 200 OK

        {
            "count": 1023
            "next": "https://api.example.org/accounts/?page=5",
            "previous": "https://api.example.org/accounts/?page=3",
            "results": [
            …
            ]
        }
    """

    def __init__(self, app, entries, per_page, page, endpoint):
        self.app = app
        self.entries = entries
        self.per_page = per_page
        self.page = page
        self.endpoint = endpoint
        self.max_page = math.ceil(len(self.entries) / self.per_page)

    @cached_property
    def count(self):
        return len(self.entries)

    @cached_property
    def results(self):
        return self.entries[
            (
                (self.page - 1) * self.per_page
            ):(((self.page - 1) * self.per_page)+self.per_page)
        ]

    has_previous = property(lambda x: x.page > 1)
    has_next = property(lambda x: x.page < x.pages)
    previous = property(
        lambda x: url_for(x.endpoint, page=x.page - 1) if (x.page - 1 > 0) else x.app.url_for(x.endpoint)  # noqa
    )
    next = property(
        lambda x: url_for(x.endpoint, page=x.page + 1) if x.page < x.max_page else x.app.url_for(x.endpoint, page=x.max_page)  # noqa
    )
    pages = property(lambda x: max(0, x.count - 1) // x.per_page + 1)


def auth_protected(some_function):
    def wrapper_check_auth(api, request, recipe_id=None):
        authorization_header = request.headers.get('authorization')
        auth = None
        if authorization_header:
            access_token = authorization_header.replace('Bearer ', '')
            auth = jwt.decode(access_token, 'secret', algorithm='HS256')
        if not auth or not api.check_auth(auth['username'], auth['password']):
            return api.auth_required(request)
        if recipe_id:
            return some_function(api, request, recipe_id)
        return some_function(api, request)
    return wrapper_check_auth
