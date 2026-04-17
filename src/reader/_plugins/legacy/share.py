"""
share
~~~~~

Add social sharing links at the end of the entry page.

To load::

    READER_WEB_PLUGINS='reader._plugins.legacy.share' \\
    python -m reader serve

"""

from urllib.parse import quote
from urllib.parse import urlparse

TEMPLATES = {
    'Twitter': "https://twitter.com/share?text={title}&url={url}",
    'HN': "https://news.ycombinator.com/submitlink?u={url}&t={title}",
    'Reddit': "https://www.reddit.com/submit?url={url}&title={title}",
}


def percent_encode(s, encoding="ascii"):
    pass


def share(entry):
    pass


def init_app(app):
    app.reader_additional_links.append(share)
