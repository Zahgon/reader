# Support for the Atom, RSS, RDF, and CDF feed formats
# Copyright 2010-2023 Kurt McKee <contactme@kurtmckee.org>
# Copyright 2002-2008 Mark Pilgrim
# All rights reserved.
#
# This file is a part of feedparser.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import copy

from ..datetimes import _parse_date
from ..urls import make_safe_absolute_uri
from ..util import FeedParserDict


class Namespace:
    """Support for the Atom, RSS, RDF, and CDF feed formats.

    The feed formats all share common elements, some of which have conflicting
    interpretations. For simplicity, all of the base feed format support is
    collected here.
    """

    supported_namespaces = {
        "": "",
        "http://backend.userland.com/rss": "",
        "http://blogs.law.harvard.edu/tech/rss": "",
        "http://purl.org/rss/1.0/": "",
        "http://my.netscape.com/rdf/simple/0.9/": "",
        "http://example.com/newformat#": "",
        "http://example.com/necho": "",
        "http://purl.org/echo/": "",
        "uri/of/echo/namespace#": "",
        "http://purl.org/pie/": "",
        "http://purl.org/atom/ns#": "",
        "http://www.w3.org/2005/Atom": "",
        "http://purl.org/rss/1.0/modules/rss091#": "",
    }

    def _start_rss(self, attrs_d):
        pass

    def _start_channel(self, attrs_d):
        pass

    def _cdf_common(self, attrs_d):
        pass

    def _start_feed(self, attrs_d):
        pass

    def _end_channel(self):
        pass

    _end_feed = _end_channel

    def _start_image(self, attrs_d):
        pass

    def _end_image(self):
        pass

    def _start_textinput(self, attrs_d):
        pass

    _start_textInput = _start_textinput

    def _end_textinput(self):
        pass

    _end_textInput = _end_textinput

    def _start_author(self, attrs_d):
        pass

    _start_managingeditor = _start_author

    def _end_author(self):
        pass

    _end_managingeditor = _end_author

    def _start_contributor(self, attrs_d):
        pass

    def _end_contributor(self):
        pass

    def _start_name(self, attrs_d):
        pass

    def _end_name(self):
        pass

    def _start_width(self, attrs_d):
        pass

    def _end_width(self):
        pass

    def _start_height(self, attrs_d):
        pass

    def _end_height(self):
        pass

    def _start_url(self, attrs_d):
        pass

    _start_homepage = _start_url
    _start_uri = _start_url

    def _end_url(self):
        pass

    _end_homepage = _end_url
    _end_uri = _end_url

    def _start_email(self, attrs_d):
        pass

    def _end_email(self):
        pass

    def _start_subtitle(self, attrs_d):
        pass

    _start_tagline = _start_subtitle

    def _end_subtitle(self):
        pass

    _end_tagline = _end_subtitle

    def _start_rights(self, attrs_d):
        pass

    _start_copyright = _start_rights

    def _end_rights(self):
        pass

    _end_copyright = _end_rights

    def _start_item(self, attrs_d):
        pass

    _start_entry = _start_item

    def _end_item(self):
        pass

    _end_entry = _end_item

    def _start_language(self, attrs_d):
        pass

    def _end_language(self):
        pass

    def _start_webmaster(self, attrs_d):
        pass

    def _end_webmaster(self):
        pass

    def _start_published(self, attrs_d):
        pass

    _start_issued = _start_published
    _start_pubdate = _start_published

    def _end_published(self):
        pass

    _end_issued = _end_published
    _end_pubdate = _end_published

    def _start_updated(self, attrs_d):
        pass

    _start_modified = _start_updated
    _start_lastbuilddate = _start_updated

    def _end_updated(self):
        pass

    _end_modified = _end_updated
    _end_lastbuilddate = _end_updated

    def _start_created(self, attrs_d):
        pass

    def _end_created(self):
        pass

    def _start_expirationdate(self, attrs_d):
        pass

    def _end_expirationdate(self):
        pass

    def _start_category(self, attrs_d):
        pass

    _start_keywords = _start_category

    def _end_category(self):
        pass

    _end_keywords = _end_category

    def _start_cloud(self, attrs_d):
        pass

    def _start_link(self, attrs_d):
        pass

    def _end_link(self):
        pass

    def _start_guid(self, attrs_d):
        pass

    _start_id = _start_guid

    def _end_guid(self):
        pass

    _end_id = _end_guid

    def _start_title(self, attrs_d):
        pass

    def _end_title(self):
        pass

    def _start_description(self, attrs_d):
        pass

    def _start_abstract(self, attrs_d):
        pass

    def _end_description(self):
        pass

    _end_abstract = _end_description

    def _start_info(self, attrs_d):
        pass

    _start_feedburner_browserfriendly = _start_info

    def _end_info(self):
        pass

    _end_feedburner_browserfriendly = _end_info

    def _start_generator(self, attrs_d):
        pass

    def _end_generator(self):
        pass

    def _start_summary(self, attrs_d):
        pass

    def _end_summary(self):
        pass

    def _start_enclosure(self, attrs_d):
        pass

    def _start_source(self, attrs_d):
        pass

    def _end_source(self):
        pass

    def _start_content(self, attrs_d):
        pass

    def _start_body(self, attrs_d):
        pass

    _start_xhtml_body = _start_body

    def _start_content_encoded(self, attrs_d):
        pass

    _start_fullitem = _start_content_encoded

    def _end_content(self):
        pass

    _end_body = _end_content
    _end_xhtml_body = _end_content
    _end_content_encoded = _end_content
    _end_fullitem = _end_content

    def _start_newlocation(self, attrs_d):
        pass

    def _end_newlocation(self):
        pass
