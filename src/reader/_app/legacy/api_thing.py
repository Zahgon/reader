"""
A thing to build APIs that work both with old-style forms and with JSON.

Contains no business logic.

See scripts/jscontrols.py for a minimal usage example.

"""

from urllib.parse import urljoin
from urllib.parse import urlparse

from flask import flash
from flask import get_flashed_messages
from flask import jsonify
from flask import redirect
from flask import request
from werkzeug.datastructures import MultiDict


def is_safe_url(target):
    pass


def redirect_to_referrer():
    pass


def get_flashed_messages_by_prefix(*prefixes):
    pass


class APIError(Exception):
    def __init__(self, message, category=None):
        super().__init__(message)
        self.message = message
        if category is not None:
            if not isinstance(category, tuple):
                category = (category,)
        self.category = category


class APIThing:
    def __init__(self, app_or_blueprint, rule, endpoint):
        self.actions = {}
        self.really = {}
        app_or_blueprint.add_url_rule(
            rule, endpoint, methods=['POST'], view_func=self.dispatch
        )
        (
            getattr(app_or_blueprint, 'add_app_template_global', None)
            or app_or_blueprint.add_template_global
        )(get_flashed_messages_by_prefix)

    def dispatch_form(self):
        pass

    def dispatch_json(self):
        pass

    def dispatch(self):
        pass

    def __call__(self, func=None, *, name=None, really=False):
        def register(f, name=name):
            if name is None:
                name = f.__name__.replace('_', '-')
            self.actions[name] = f
            self.really[f] = really
            return f

        if func is None:
            return register
        return register(func)
