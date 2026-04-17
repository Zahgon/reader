# Support for the iTunes format
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
        "http://www.itunes.com/DTDs/PodCast-1.0.dtd": "itunes",
        # Extra namespace
        "http://example.com/DTDs/PodCast-1.0.dtd": "itunes",
    }

    def _start_itunes_author(self, attrs_d):
        pass

    def _end_itunes_author(self):
        pass

    def _end_itunes_category(self):
        pass

    def _start_itunes_name(self, attrs_d):
        pass

    def _end_itunes_name(self):
        pass

    def _start_itunes_email(self, attrs_d):
        pass

    def _end_itunes_email(self):
        pass

    def _start_itunes_subtitle(self, attrs_d):
        pass

    def _end_itunes_subtitle(self):
        pass

    def _start_itunes_summary(self, attrs_d):
        pass

    def _end_itunes_summary(self):
        pass

    def _start_itunes_owner(self, attrs_d):
        pass

    def _end_itunes_owner(self):
        pass

    def _end_itunes_keywords(self):
        pass

    def _start_itunes_category(self, attrs_d):
        pass

    def _start_itunes_image(self, attrs_d):
        pass

    _start_itunes_link = _start_itunes_image

    def _end_itunes_block(self):
        pass

    def _end_itunes_explicit(self):
        pass
