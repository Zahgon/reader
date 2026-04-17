# Support for the Media RSS format
# Copyright 2010-2023 Kurt McKee <contactme@kurtmckee.org>
# Copyright 2002-2008 Mark Pilgrim
# All rights reserved.
#
# This file is a part of feedparser.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
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

from ..util import FeedParserDict


class Namespace:
    supported_namespaces = {
        # Canonical namespace
        "http://search.yahoo.com/mrss/": "media",
        # Old namespace (no trailing slash)
        "http://search.yahoo.com/mrss": "media",
    }

    def _start_media_category(self, attrs_d):
        pass

    def _end_media_category(self):
        pass

    def _end_media_keywords(self):
        pass

    def _start_media_title(self, attrs_d):
        pass

    def _end_media_title(self):
        pass

    def _start_media_group(self, attrs_d):
        # don't do anything, but don't break the enclosed tags either
        pass

    def _start_media_rating(self, attrs_d):
        pass

    def _end_media_rating(self):
        pass

    def _start_media_credit(self, attrs_d):
        pass

    def _end_media_credit(self):
        pass

    def _start_media_description(self, attrs_d):
        pass

    def _end_media_description(self):
        pass

    def _start_media_restriction(self, attrs_d):
        pass

    def _end_media_restriction(self):
        pass

    def _start_media_license(self, attrs_d):
        pass

    def _end_media_license(self):
        pass

    def _start_media_content(self, attrs_d):
        pass

    def _start_media_thumbnail(self, attrs_d):
        pass

    def _end_media_thumbnail(self):
        pass

    def _start_media_player(self, attrs_d):
        pass

    def _end_media_player(self):
        pass
