import pathlib
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from functools import lru_cache
from urllib.parse import urlparse

import humanize
from flask import abort
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import Flask
from flask import get_flashed_messages
from flask import redirect
from flask import render_template
from flask import render_template_string
from flask import request
from flask import Response
from flask import stream_with_context
from flask import url_for
from flask_wtf.csrf import CSRFError
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from jinja2_fragments.flask import render_block
from werkzeug.exceptions import NotFound

from reader import EntryNotFoundError
from reader import FeedExistsError
from reader import FeedNotFoundError
from reader import InvalidFeedURLError
from reader import UpdateError

from .ext import get_reader
from .ext import ReaderExtension
from .forms import AddFeed
from .forms import ChangeFeedTitle
from .forms import EntryFilter
from .forms import FeedFilter

# for a prototype with tags and search support, see
# https://github.com/lemon24/reader/tree/3.21/src/reader/_app/v2


blueprint = Blueprint(
    'reader', __name__, static_folder='static', template_folder='templates'
)


@blueprint.errorhandler(FeedNotFoundError)
def handle_feed_not_found(e):
    pass


@blueprint.errorhandler(EntryNotFoundError)
def handle_entry_not_found(e):
    pass


@blueprint.errorhandler(CSRFError)
def handle_csrf_error(error):
    pass


CSRF_ERROR_TEMPLATE = """\
<ul class="list-unstyled">
  <li class="alert alert-danger">
    {{ error.description }}
    <a href="javascript:document.location.reload()">Refresh</a> and try again.
  </li>
</ul>
"""


@blueprint.route('/')
def entries():
    pass


@blueprint.route('/entry-actions', methods=['POST'])
def entry_actions():
    pass


@blueprint.route('/feeds')
def feeds():
    pass


@blueprint.route('/feed-actions', methods=['POST'])
def feed_actions():
    pass


@blueprint.route('/feeds/delete', methods=['GET', 'POST'])
def delete_feed():
    reader = get_reader()
    feed = reader.get_feed(request.args['feed'])

    if request.method == 'POST':
        reader.delete_feed(feed)
        flash(f"Deleted feed {feed.resolved_title or feed.url}.", 'success')
        return redirect(url_for('.feeds'), code=303)

    return render_template('delete_feed.html', feed=feed)


@blueprint.route('/feeds/title', methods=['GET', 'POST'])
def change_feed_title():
    pass


@blueprint.route('/feeds/add', methods=['GET', 'POST'])
def add_feed():
    reader = get_reader()
    form = AddFeed(request.form)

    if request.method == 'POST' and form.validate():
        url = form.feed.data

        try:
            reader.add_feed(url)
        except InvalidFeedURLError as e:
            form.feed.errors.append(f"invalid feed: {e}")
        except FeedExistsError:
            flash("Feed already exists.", 'secondary')
            return redirect(url_for('.entries', feed=url), code=303)
        else:
            # TODO: updating should be out of band
            try:
                reader.update_feed(url)
            except UpdateError:
                pass
            else:
                flash("Added and updated feed.", 'success')
            return redirect(url_for('.entries', feed=url), code=303)

    return render_template('add_feed.html', form=form)


@blueprint.route('/entry')
def entry():
    reader = get_reader()
    entry = reader.get_entry((request.args['feed'], request.args['entry']))
    return render_template('entry.html', entry=entry)


def stream_template(template_name_or_list, **kwargs):
    # Ensure flashed messages get removed from the session,
    # otherwise they keep adding up and never disappear.
    # Assumes the template will call get_flashed_messages() at some point.
    # https://github.com/lemon24/reader/issues/81
    pass


@blueprint.app_template_filter()
def humanize_naturaltime(dt):
    pass


@blueprint.record_once
def add_jinja_do_extension(setup_state):
    pass


@blueprint.app_template_global()
def find_static(filename, blueprint=None):
    pass


@lru_cache
def _find_static(folder, filename):
    pass


def create_app(reader_config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    CSRFProtect(app)

    app.config['READER'] = reader_config
    ReaderExtension(app)

    app.register_blueprint(blueprint)

    return app
