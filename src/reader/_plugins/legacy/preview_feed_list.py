"""
preview_feed_list
~~~~~~~~~~~~~~~~~

If the feed to be previewed is not actually a feed,
show a list of feeds linked from that URL (if any).

This plugin needs additional dependencies, use the ``unstable-plugins`` extra
to install them:

.. code-block:: bash

    pip install reader[unstable-plugins]

To load::

    READER_WEB_PLUGINS='reader._plugins.legacy.preview_feed_list' \\
    python -m reader serve

Implemented for https://github.com/lemon24/reader/issues/150.

"""

import traceback
import urllib.parse
import warnings

import bs4
import requests
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from reader._app.legacy import get_reader
from reader._app.legacy import got_preview_parse_error

blueprint = Blueprint('preview_feed_list', __name__, template_folder='templates')


ATTRS = ['type', 'href', 'title', 'text']
MARKERS = ['rss', 'atom', 'feed']

SELECTORS = [
    'link[href][rel=alternate], meta[href][name=alternate], link[href][rel=alternative]',
    # fallback
    'a[href]',
]


warnings.filterwarnings(
    'ignore',
    message='No parser was explicitly specified',
    module='reader._plugins.preview_feed_list',
)


def get_alternates(content, url):
    soup = bs4.BeautifulSoup(content)
    for selector in SELECTORS:
        alternates = list(_get_alternates(soup, url, selector))
        if alternates:
            return alternates
    return []


def _get_alternates(soup, url, selector):
    for element in soup.select(selector):
        attrs = dict(element.attrs)

        href = attrs.get('href')
        if not href:
            continue

        text = ' '.join(element.stripped_strings)
        if text:
            attrs['text'] = text

        for attr in ATTRS:
            value = attrs.get(attr, '').lower()
            if any(marker in value for marker in MARKERS):
                break
        else:
            continue

        # this may not work correctly for relative paths, e.g. should
        # http://example.com/foo + bar.xml result in
        # http://example.com/bar.xml (now) or
        # http://example.com/foo/bar.xml?
        rv = {'href': urllib.parse.urljoin(url, attrs['href'])}

        if 'type' in attrs:
            rv['type'] = attrs['type']
        if 'text' in attrs:
            rv['title'] = attrs['text']
        elif 'title' in attrs:
            rv['title'] = attrs['title']

        yield rv


@blueprint.route('/preview-feed-list')
def feed_list():
    pass


class GotPreviewParseError(Exception):
    """Signaling exception used to intercept /preview ParseError"""


@got_preview_parse_error.connect
def raise_got_preview_parse_error(error):
    # TODO: ParseError should be more specific, it should be clear if retrieving or parsing failed
    pass


@blueprint.app_errorhandler(GotPreviewParseError)
def handle_parse_error_i_guess(error):
    pass


def init_app(app):
    app.register_blueprint(blueprint)
