"""
.. _reader-ua-fallback:

.ua_fallback
~~~~~~~~~~~~

Retry feed requests that get ``403 Forbidden``
with a different user agent.

Sometimes, servers blocks requests coming from *reader*
based on the user agent.
This plugin retries the request with feedparser's user agent,
which seems to be more widely accepted.

Servers/CDNs known to not accept the *reader* UA: Cloudflare, WP Engine.

.. todo::

    Maybe cache if the fallback is needed as reader metadata,
    and change the UA on the first request instead of retrying.

..
    Implemented for https://github.com/lemon24/reader/issues/181

"""

import logging

_LOG_HEADERS = ['Server', 'X-Powered-By']

log = logging.getLogger(__name__)


def _ua_fallback_response_hook(session, response, request, **kwargs):
    pass


def init_reader(reader):
    reader._parser.session_factory.response_hooks.append(_ua_fallback_response_hook)
