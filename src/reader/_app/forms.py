from dataclasses import dataclass

import yaml
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import HiddenField
from wtforms import RadioField
from wtforms import SearchField
from wtforms import StringField
from wtforms import URLField
from wtforms import validators

from reader._types import tag_filter_argument


class TagFilterField(StringField):

    def process_formdata(self, valuelist):
        pass

    def _value(self):
        pass


class HiddenEntryField(HiddenField):

    def process_formdata(self, valuelist):
        pass

    def _value(self):
        pass


class PresetsMixin:
    PRESETS_INCLUDE = set()
    PRESETS_EXCLUDE = set()
    PRESETS = {}

    @property
    def presets(self):
        pass

    @property
    def active_presets(self):
        pass

    @property
    def args(self):
        pass

    def replace(self, **kwargs):
        return type(self)(data=self.data, **kwargs)


@dataclass
class Preset:
    name: str
    args: dict[str, str]
    active: bool = False


def get_formdata(field):
    pass


def radio_field(*args, choices, **kwargs):
    """Like RadioField, but choices is a list of (value, value_str),
    (value, value_str, label), or (value, value_str, label, render_kw) tuples.

    """
    return RadioField(
        *args,
        choices=[c[1] if len(c) == 2 else c[1:] for c in choices],
        coerce=({c[1]: c[0] for c in choices} | {c[0]: c[0] for c in choices}).get,
        **kwargs,
    )


BOOL_CHOICES = [(True, 'yes'), (False, 'no'), (None, 'all')]
TRISTATE_CHOICES = [('notfalse', 'maybe')] + BOOL_CHOICES
ENTRY_SORT_CHOICES = ['recent', 'random']


class EntryFilter(PresetsMixin, Form):
    feed = HiddenField("feed")
    starting_after = HiddenEntryField(name="after")
    # search = SearchField("search", name='Q')
    # feed_tags = TagFilterField("feed tags", name='tags')
    # tags = TagFilterField("entry tags", name='entry-tags')
    read = radio_field("read", choices=BOOL_CHOICES, default='no')
    important = radio_field("important", choices=TRISTATE_CHOICES, default='maybe')
    has_enclosures = radio_field(
        "enclosures", name='enclosures', choices=BOOL_CHOICES, default='all'
    )
    sort = RadioField("sort", choices=ENTRY_SORT_CHOICES, default='recent')

    PRESETS_INCLUDE = {'read', 'important', 'enclosures', 'sort'}
    PRESETS_EXCLUDE = {'after'}
    PRESETS = {
        'unread': {},
        'important': {'read': 'all', 'important': 'yes'},
        'podcast': {'enclosures': 'yes'},
        'random': {'sort': 'random'},
    }


class SearchEntryFilter(EntryFilter):
    search = SearchField("search", name='q')
    sort = RadioField(
        "sort", choices=['relevant'] + ENTRY_SORT_CHOICES, default='relevant'
    )


FEED_SORT_CHOICES = ['title', 'added']


class FeedFilter(PresetsMixin, Form):
    broken = radio_field("broken", choices=BOOL_CHOICES, default='all')
    updates_enabled = radio_field(
        "enabled", name='enabled', choices=BOOL_CHOICES, default='all'
    )
    sort = RadioField("sort", choices=FEED_SORT_CHOICES, default='title')

    PRESETS_INCLUDE = {'broken', 'enabled', 'sort'}
    PRESETS = {
        'all': {},
        'added': {'sort': 'added'},
        'broken': {'broken': 'yes', 'enabled': 'yes'},
        'disabled': {'enabled': 'no'},
    }


class AddFeed(FlaskForm):
    feed = URLField('URL', [validators.DataRequired(), validators.URL()])


class ChangeFeedTitle(FlaskForm):
    title = StringField('title', filters=[lambda s: (s or '').strip() or None])


if __name__ == '__main__':
    from werkzeug.datastructures import MultiDict

    args = MultiDict(dict(read=False, after='a\0b'))
    form = EntryFilter(args)
    print(form.data)
    print(form.args)
    for preset in form.presets:
        print(preset)

    # import IPython; IPython.embed()
