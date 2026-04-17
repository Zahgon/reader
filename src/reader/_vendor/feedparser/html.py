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

import html.entities
import re

# These items must all be imported into this module due to .__code__ replacements.
from .sgml import (  # noqa: F401
    attrfind,
    charref,
    endbracket,
    entityref,
    incomplete,
    interesting,
    sgmllib,
    shorttag,
    shorttagopen,
    starttagopen,
    tagfind,
)

_cp1252 = {
    128: "\u20ac",  # euro sign
    130: "\u201a",  # single low-9 quotation mark
    131: "\u0192",  # latin small letter f with hook
    132: "\u201e",  # double low-9 quotation mark
    133: "\u2026",  # horizontal ellipsis
    134: "\u2020",  # dagger
    135: "\u2021",  # double dagger
    136: "\u02c6",  # modifier letter circumflex accent
    137: "\u2030",  # per mille sign
    138: "\u0160",  # latin capital letter s with caron
    139: "\u2039",  # single left-pointing angle quotation mark
    140: "\u0152",  # latin capital ligature oe
    142: "\u017d",  # latin capital letter z with caron
    145: "\u2018",  # left single quotation mark
    146: "\u2019",  # right single quotation mark
    147: "\u201c",  # left double quotation mark
    148: "\u201d",  # right double quotation mark
    149: "\u2022",  # bullet
    150: "\u2013",  # en dash
    151: "\u2014",  # em dash
    152: "\u02dc",  # small tilde
    153: "\u2122",  # trade mark sign
    154: "\u0161",  # latin small letter s with caron
    155: "\u203a",  # single right-pointing angle quotation mark
    156: "\u0153",  # latin small ligature oe
    158: "\u017e",  # latin small letter z with caron
    159: "\u0178",  # latin capital letter y with diaeresis
}


class BaseHTMLProcessor(sgmllib.SGMLParser):
    special = re.compile("""[<>'"]""")
    bare_ampersand = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|\w+;)")
    elements_no_end_tag = {
        "area",
        "base",
        "basefont",
        "br",
        "col",
        "command",
        "embed",
        "frame",
        "hr",
        "img",
        "input",
        "isindex",
        "keygen",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }

    def __init__(self, encoding=None, _type="application/xhtml+xml"):
        if encoding:
            self.encoding = encoding
        self._type = _type
        self.pieces = []
        super().__init__()

    def reset(self):
        self.pieces = []
        super().reset()

    def _shorttag_replace(self, match):
        """
        :type match: Match[str]
        :rtype: str
        """
        pass

    # By declaring these methods and overriding their compiled code
    # with the code from sgmllib, the original code will execute in
    # feedparser's scope instead of sgmllib's. This means that the
    # `tagfind` and `charref` regular expressions will be found as
    # they're declared above, not as they're declared in sgmllib.
    def goahead(self, i):
        raise NotImplementedError

    # Replace goahead with SGMLParser's goahead() code object.
    goahead.__code__ = sgmllib.SGMLParser.goahead.__code__

    def __parse_starttag(self, i):
        raise NotImplementedError

    # Replace __parse_starttag with SGMLParser's parse_starttag() code object.
    __parse_starttag.__code__ = sgmllib.SGMLParser.parse_starttag.__code__

    def parse_starttag(self, i):
        pass

    def feed(self, data):
        """
        :type data: str
        :rtype: None
        """

        data = re.sub(r"<!((?!DOCTYPE|--|\[))", r"&lt;!\1", data, flags=re.IGNORECASE)
        data = re.sub(r"<([^<>\s]+?)\s*/>", self._shorttag_replace, data)
        data = data.replace("&#39;", "'")
        data = data.replace("&#34;", '"')
        super().feed(data)
        super().close()

    @staticmethod
    def normalize_attrs(attrs):
        """
        :type attrs: List[Tuple[str, str]]
        :rtype: List[Tuple[str, str]]
        """
        pass

    def unknown_starttag(self, tag, attrs):
        """
        :type tag: str
        :type attrs: List[Tuple[str, str]]
        :rtype: None
        """
        pass

    def unknown_endtag(self, tag):
        """
        :type tag: str
        :rtype: None
        """
        pass

    def handle_charref(self, ref):
        """
        :type ref: str
        :rtype: None
        """
        pass

    def handle_entityref(self, ref):
        """
        :type ref: str
        :rtype: None
        """
        pass

    def handle_data(self, text):
        """
        :type text: str
        :rtype: None
        """
        pass

    def handle_comment(self, text):
        """
        :type text: str
        :rtype: None
        """
        pass

    def handle_pi(self, text):
        """
        :type text: str
        :rtype: None
        """
        pass

    def handle_decl(self, text):
        """
        :type text: str
        :rtype: None
        """
        pass

    _new_declname_match = re.compile(r"[a-zA-Z][-_.a-zA-Z0-9:]*\s*").match

    def _scan_name(self, i, declstartpos):
        """
        :type i: int
        :type declstartpos: int
        :rtype: Tuple[Optional[str], int]
        """
        pass

    def convert_charref(self, name):
        """
        :type name: str
        :rtype: str
        """
        pass

    def convert_entityref(self, name):
        """
        :type name: str
        :rtype: str
        """
        pass

    def output(self):
        """Return processed HTML as a single string.

        :rtype: str
        """

        return "".join(self.pieces)

    def parse_declaration(self, i):
        """
        :type i: int
        :rtype: int
        """
        pass
