import sqlite3

from ._sql_utils import parse_schema
from ._sqlite_utils import ddl_transaction
from ._sqlite_utils import HeavyMigration

SCHEMA = parse_schema("""

CREATE TABLE feeds (

    -- feed data
    url TEXT PRIMARY KEY NOT NULL,
    title TEXT,
    link TEXT,
    updated TIMESTAMP,
    author TEXT,
    subtitle TEXT,
    version TEXT,
    user_title TEXT,  -- except this one, which comes from reader
    caching_info TEXT,
    data_hash BLOB,  -- derived from feed data

    -- reader data
    stale INTEGER NOT NULL DEFAULT 0,
    updates_enabled INTEGER NOT NULL DEFAULT 1,
    update_after TIMESTAMP,  -- null if the feed was never retrieved
    last_retrieved TIMESTAMP,  -- null if the feed was never retrieved
    last_updated TIMESTAMP,  -- null if the feed was never updated
    added TIMESTAMP NOT NULL,
    last_exception TEXT

    -- NOTE: when adding new fields, check if they should be set
    -- to their default value in change_feed_url()
);


CREATE TABLE entries (

    -- entry data
    id TEXT NOT NULL,
    feed TEXT NOT NULL,
    title TEXT,
    link TEXT,
    updated TIMESTAMP,
    author TEXT,
    published TIMESTAMP,
    summary TEXT,
    content TEXT,
    enclosures TEXT,
    source TEXT,
    original_feed TEXT,  -- null if the feed was never moved
    data_hash BLOB,  -- derived from entry data
    data_hash_changed INTEGER,  -- metadata about data_hash

    -- reader data
    read INTEGER,
    read_modified TIMESTAMP,
    important INTEGER,
    important_modified TIMESTAMP,
    added_by TEXT NOT NULL,
    last_updated TIMESTAMP NOT NULL,
    first_updated TIMESTAMP NOT NULL,
    first_updated_epoch TIMESTAMP NOT NULL,
    feed_order INTEGER NOT NULL,
    recent_sort TIMESTAMP NOT NULL,
    sequence BLOB,

    PRIMARY KEY (id, feed),
    FOREIGN KEY (feed) REFERENCES feeds(url)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE global_tags (
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    PRIMARY KEY (key)
);

CREATE TABLE feed_tags (
    feed TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT NOT NULL,

    PRIMARY KEY (feed, key),
    FOREIGN KEY (feed) REFERENCES feeds(url)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE entry_tags (
    id TEXT NOT NULL,
    feed TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT NOT NULL,

    PRIMARY KEY (id, feed, key),
    FOREIGN KEY (id, feed) REFERENCES entries(id, feed)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- speed up get_entries() queries that use apply_recent()
CREATE INDEX entries_by_recent ON entries (
    recent_sort DESC,
    coalesce(published, updated, first_updated) DESC,
    feed DESC,
    last_updated DESC,
    - feed_order DESC,
    id DESC
);

-- speed up get_entry_counts(feed=...)
CREATE INDEX entries_by_feed ON entries (feed);

-- speed up simple get_feeds(tags=...) and get_entries(tags=...) forms
-- (see reader._storage._tags.by_key_filter docstring for details)
CREATE INDEX feed_tags_by_key ON feed_tags(key);
CREATE INDEX entry_tags_by_key ON entry_tags(key);

""")  # fmt: skip

feeds_table = SCHEMA['table']['feeds']
entries_table = SCHEMA['table']['entries']
global_tags_table = SCHEMA['table']['global_tags']
feed_tags_table = SCHEMA['table']['feed_tags']
entry_tags_table = SCHEMA['table']['entry_tags']

entries_by_recent_index = SCHEMA['index']['entries_by_recent']
entries_by_feed_index = SCHEMA['index']['entries_by_feed']
feed_tags_by_key_index = SCHEMA['index']['feed_tags_by_key']
entry_tags_by_key_index = SCHEMA['index']['entry_tags_by_key']


def create_all(db: sqlite3.Connection) -> None:
    pass


def create_indexes(db: sqlite3.Connection) -> None:
    pass


def update_from_36_to_37(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # for https://github.com/lemon24/reader/issues/279
    pass


def update_from_37_to_38(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/254#issuecomment-1404215814

    pass
    # pre-3.12 (version 38), we'd re-create the entries search triggers here;
    # no point in doing that anymore, update_from_38_to_39 drops them anyway


def update_from_38_to_39(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/323

    pass


def update_from_39_to_40(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/332
    pass


def update_from_40_to_41(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/307

    pass


def update_from_41_to_42(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/359
    pass


def update_from_42_to_43(db: sqlite3.Connection, /) -> None:  # pragma: no cover
    # https://github.com/lemon24/reader/issues/276
    pass


VERSION = 43

MIGRATIONS = {
    # 1-9 removed before 0.1 (last in e4769d8ba77c61ec1fe2fbe99839e1826c17ace7)
    # 10-16 removed before 1.0 (last in 618f158ebc0034eefb724a55a84937d21c93c1a7)
    # 17-28 removed before 2.0 (last in be9c89581ea491d0c9cc95c9d39f073168a2fd02)
    # 29-35 removed before 3.0 (last in 69c75529a3f80107b68346d592d6450f9725187c)
    36: update_from_36_to_37,
    37: update_from_37_to_38,
    38: update_from_38_to_39,
    39: update_from_39_to_40,
    40: update_from_40_to_41,
    41: update_from_41_to_42,
    42: update_from_42_to_43,
}
MISSING_SUFFIX = (
    "; you may have skipped some required migrations, see "
    "https://reader.readthedocs.io/en/latest/changelog.html#removed-migrations-3-0"
)

MIGRATION = HeavyMigration(create_all, VERSION, MIGRATIONS, MISSING_SUFFIX)
