"""
.. _reader-mark-as-read:

.mark_as_read
~~~~~~~~~~~~~

.. module:: reader
  :no-index:

Mark added entries of specific feeds as read + unimportant
if their title matches a regex.

To configure, set the ``make_reader_reserved_name('mark-as-read')``
(by default, ``.reader.mark-as-read``)
tag to something like::

    {
        "title": ["first-regex", "second-regex"]
    }

By default, this plugin runs only for newly-added entries.
To run it for the existing entries of a feed,
add the ``.reader.mark-as-read.once`` tag to the feed;
the plugin will run on the next feed update, and remove the tag afterwards.


.. versionchanged:: 2.4
    Explicitly mark matching entries as unimportant.

.. versionchanged:: 2.7
    Use the ``.reader.mark-as-read`` metadata for configuration.
    Feeds using the old metadata, ``.reader.mark_as_read``,
    will be migrated automatically on update until `reader` 3.0.

.. versionchanged:: 3.5
    Don't set :attr:`~reader.Entry.read_modified` and
    :attr:`~reader.Entry.important_modified` anymore;
    because :attr:`~reader.Entry.important` is now optional,
    ``important = False`` is enough to mark an entry as unimportant.
    Old unimportant entries will be migrated automatically.

.. versionchanged:: 3.13
    Make it possible to re-run the plugin for existing entries.


.. todo::

    Possible optimizations:

    1.  Add the entry directly as read instead of marking it afterwards
        (requires a new hook to process the entry before it is added,
        and Storage support).

..
    Implemented for https://github.com/lemon24/reader/issues/79.

"""

import logging
import re

from reader.exceptions import EntryNotFoundError
from reader.exceptions import TagNotFoundError
from reader.types import EntryUpdateStatus

# avoid circular imports

log = logging.getLogger(__name__)


def _get_config(reader, feed_url, key, patterns_key):
    pass


_CONFIG_TAG = 'mark-as-read'
_ONCE_TAG = _CONFIG_TAG + '.once'


def _mark_as_read(reader, entry, status):
    pass


def _mark_as_read_backfill(reader, feed):
    pass


def init_reader(reader):
    reader.before_feed_update_hooks.append(_mark_as_read_backfill)
    reader.after_entry_update_hooks.append(_mark_as_read)
