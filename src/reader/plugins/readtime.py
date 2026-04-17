"""
.. _reader-readtime:

.readtime
~~~~~~~~~

.. module:: reader
  :no-index:

Calculate the read time for new/updated entries,
and store it as the ``.reader.readtime`` entry tag, with the format::

    {'seconds': 1234}

The content used is that returned by :meth:`~Entry.get_content`.


The read time for existing entries is backfilled as follows:

* On the first :meth:`~Reader.update_feeds` / :meth:`~Reader.update_feeds_iter` call:

  * all feeds with :attr:`~Feed.updates_disabled` false are scheduled to be backfilled

    * the feeds selected to be updated are backfilled then
    * the feeds not selected to be updated will be backfilled
      the next time they are updated

  * all feeds with :attr:`~Feed.updates_disabled` true are backfilled,
    regardless of which feeds are selected to be updated

* To prevent any feeds from being backfilled,
  set the ``.reader.readtime`` global tag to ``{'backfill': 'done'}``.
* To schedule a feed to be backfilled on its next update,
  set the ``.reader.readtime`` feed tag to ``{'backfill': 'pending'}``.


.. versionadded:: 2.12

.. versionchanged:: 3.1

    Do not require additional dependencies.
    Deprecate the ``readtime`` extra.


..
    Implemented for https://github.com/lemon24/reader/issues/275

"""

import logging
import math
import re

from reader._storage._html_utils import get_soup
from reader._storage._html_utils import remove_nontext_elements
from reader.exceptions import EntryNotFoundError
from reader.types import _get_entry_content

log = logging.getLogger('reader.plugins.readtime')


_TAG = 'readtime'


def _readtime_of_entry(entry):
    pass


# roughly following https://github.com/alanhamlett/readtime 2.0


_WPM = 265
_WORD_DELIMITER = re.compile(r'\W+')


def _readtime_of_html(html):
    pass


def _readtime_of_strings(strings):
    pass


def _after_entry_update(reader, entry, status):
    pass


def _before_feeds_update(reader):
    pass


def _after_feed_update(reader, feed):
    pass


def _after_feeds_update(reader):
    pass


def _backfill_feed(reader, feed, key):
    pass


def _set_entry_readtime(reader, entry, key):
    pass


def init_reader(reader):
    reader.after_entry_update_hooks.append(_after_entry_update)
    reader.before_feeds_update_hooks.append(_before_feeds_update)
    reader.after_feed_update_hooks.append(_after_feed_update)
    reader.after_feeds_update_hooks.append(_after_feeds_update)
