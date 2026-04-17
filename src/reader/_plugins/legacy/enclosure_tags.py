"""
enclosure_tags
~~~~~~~~~~~~~~

Fix tags for MP3 enclosures (e.g. podcasts).

Adds a "with tags" link to a version of the file with tags set as follows:

* the entry title as title
* the feed (user) title as album and artist
* `Podcast` as genre, if the feed has any tag containing "podcast"

This plugin needs additional dependencies, use the ``unstable-plugins`` extra
to install them:

.. code-block:: bash

    pip install reader[unstable-plugins]

To load::

    READER_WEB_PLUGINS='reader._plugins.legacy.enclosure_tags' \\
    python -m reader serve

Implemented for :issue:`50`.
Became a plugin in :issue:`52`.
Streaming added in :issue:`344`.

"""

import io
from urllib.parse import urlparse

import mutagen.mp3
import requests
from flask import Blueprint
from flask import request
from flask import Response
from flask import stream_with_context
from flask import url_for
from jinja2.filters import do_striptags as striptags

blueprint = Blueprint('enclosure_tags', __name__)


ALL_TAGS = ('album', 'title', 'artist', 'genre')


@blueprint.route('/enclosure-tags', defaults={'filename': None})
@blueprint.route('/enclosure-tags/<filename>')
def enclosure_tags(filename):
    pass


def update_tags_requests(url, tags, *, session=requests):
    """update_tags_requests(url, ...) -> (headers, iter_chunks())"""
    pass


def update_tags(file, tags):
    """update_tags(file, ...) -> (old_prefix, new_prefix)

    Rewrite the prefix of file to update ID3v2 tags.

    """
    pass


def enclosure_tags_filter(enclosure, entry, feed_tags):
    pass


def init_app(app):
    app.register_blueprint(blueprint)
    app.reader_additional_enclosure_links.append(enclosure_tags_filter)
