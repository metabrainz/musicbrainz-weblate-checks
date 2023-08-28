# Copyright © Michal Čihař <michal@weblate.org>
# Copyright © MetaBrainz Foundation
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""MusicBrainz format quality checks."""

import re

from django.utils.translation import gettext_lazy as _
from weblate.checks.base import TargetCheck

MUSICBRAINZ_BRACE_MATCH = re.compile(
    r"""
    {(                                  # initial {
        (?P<identifier>
            [_A-Za-z][_0-9A-Za-z]*      # identifier
        )
        (?:                             # optional replacement text
            :                           # ':' separator
            (?:
                [^{}:%|]*               # text with only one
                %                       # '%' placeholder for identifier
                [^{}:%|]*               # and more text
                |
                [^{}:%|]+               # text without any placeholder
            )
            (?:                         # optional alternative replacement text
                \|                      # '|' separator
                (?:
                    [^{}:%|]*           # text with only one
                    %                   # '%' placeholder for identifier
                    [^{}:%|]*           # and more text
                    |
                    [^{}:%|]+           # text without any placeholder
                )
            )?
        )?
    )}                                  # trailing }
    """,
    re.VERBOSE,
)


class MusicBrainzBraceCheck(TargetCheck):
    """Check braces in MusicBrainz internationalization format string."""

    # Used as identifier for check, should be unique
    # Has to be shorter than 50 chars
    check_id = "musicbrainz_brace"

    # Short name used to display failing check
    name = _("MusicBrainz brace format")

    # Description for failing check
    description = _("MusicBrainz brace format does not match source")

    def check_single(self, source, target, unit):
        """Check single target string with its source string

        Note that target string is allowed to use braces
        in any order any additional number of times (thus `set`)
        """

        source_matches = MUSICBRAINZ_BRACE_MATCH.finditer(source)
        source_identifiers = set(
            m.group('identifier') for m in source_matches
        )

        target_matches = MUSICBRAINZ_BRACE_MATCH.finditer(target)
        target_identifiers = set(
            m.group('identifier') for m in target_matches
        )

        return source_identifiers != target_identifiers
