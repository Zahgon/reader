# Support for the Dublin Core metadata extensions
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

from ..datetimes import _parse_date
from ..util import FeedParserDict


class Namespace:
    supported_namespaces = {
        "http://purl.org/dc/elements/1.1/": "dc",
        "http://purl.org/dc/terms/": "dcterms",
    }

    def _end_dc_author(self):
        pass

    def _end_dc_creator(self):
        pass

    def _end_dc_date(self):
        pass

    def _end_dc_description(self):
        pass

    def _end_dc_language(self):
        pass

    def _end_dc_publisher(self):
        pass

    def _end_dc_rights(self):
        pass

    def _end_dc_subject(self):
        pass

    def _end_dc_title(self):
        pass

    def _end_dcterms_created(self):
        pass

    def _end_dcterms_issued(self):
        pass

    def _end_dcterms_modified(self):
        pass

    def _start_dc_author(self, attrs_d):
        pass

    def _start_dc_creator(self, attrs_d):
        pass

    def _start_dc_date(self, attrs_d):
        pass

    def _start_dc_description(self, attrs_d):
        pass

    def _start_dc_language(self, attrs_d):
        pass

    def _start_dc_publisher(self, attrs_d):
        pass

    def _start_dc_rights(self, attrs_d):
        pass

    def _start_dc_subject(self, attrs_d):
        pass

    def _start_dc_title(self, attrs_d):
        pass

    def _start_dcterms_created(self, attrs_d):
        pass

    def _start_dcterms_issued(self, attrs_d):
        pass

    def _start_dcterms_modified(self, attrs_d):
        pass

    def _start_dcterms_valid(self, attrs_d):
        pass

    def _end_dcterms_valid(self):
        pass

    def _start_dc_contributor(self, attrs_d):
        pass

    def _end_dc_contributor(self):
        pass
