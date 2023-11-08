# Copyright © Michal Čihař <michal@weblate.org>
# Copyright © MetaBrainz Foundation
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Tests for MusicBrainz format quality checks."""


from .checks import MusicBrainzBraceCheck;

from weblate.checks.tests.test_checks import CheckTestCase

class MusicBrainzBraceCheckTest(CheckTestCase):
    check = MusicBrainzBraceCheck()

    def setUp(self):
        super().setUp()

    def test_no_format(self):
        self.assertFalse(
            self.check.check_single("string",
                                    "retez", None)
        )

    def test_text_format(self):
        self.assertFalse(
            self.check.check_single("{var} string",
                                    "{var} retez", None)
        )

    def test_added_duplicate_text_format(self):
        self.assertFalse(
            self.check.check_single("{var} string",
                                    "{var} retez {var}", None)
        )

    def test_skipped_duplicate_text_format(self):
        self.assertFalse(
            self.check.check_single("{var} string {var}",
                                    "{var} retez", None)
        )

    def test_missing_text_format(self):
        self.assertTrue(
            self.check.check_single("{var} string",
                                    "retez", None)
        )

    def test_misspelled_text_format(self):
        self.assertTrue(
            self.check.check_single("{var} string",
                                    "{weird} retez", None)
        )

    def test_unexpected_text_format(self):
        self.assertTrue(
            self.check.check_single("string",
                                    "{var} retez", None)
        )

    def test_text_with_substitute_format(self):
        self.assertFalse(
            self.check.check_single("{var:substitute} string",
                                    "{var:nahradnik} retez", None)
        )

    def test_text_with_substitute_and_alternative_format(self):
        self.assertFalse(
            self.check.check_single("{var:substitute|alternative} string",
                                    "{var:nahradnik|alternativa} retez", None)
        )

    def test_text_with_percent_and_alternative_format(self):
        self.assertFalse(
            self.check.check_single("{var:%|alternative} string",
                                    "{var:%|alternativa} retez", None)
        )

    def test_text_alone_to_substitute_format(self):
        self.assertFalse(
            self.check.check_single("{var} string",
                                    "{var:nahradnik} retez", None)
        )

    def test_text_alone_to_substitute_and_alternative_format(self):
        self.assertFalse(
            self.check.check_single("{var} string",
                                    "{var:nahradnik|alternativa} retez", None)
        )

    def test_text_alone_to_percent_and_alternative_format(self):
        self.assertFalse(
            self.check.check_single("{var} string",
                                    "{var:%|alternativa} retez", None)
        )

    def test_instrument_format(self):
        self.assertFalse(
            self.check.check_single("{instrument:%|instruments} string",
                                    "{instrument:%|nastroje} retez", None)
        )

    def test_instrument_missing_percent_format(self):
        self.assertTrue(
            self.check.check_single("{instrument:%|instruments} string",
                                    "{instrument:nastroj|nastroje} retez", None)
        )

    def test_instrument_missing_plural_format(self):
        self.assertTrue(
            self.check.check_single("{instrument:%|instruments} string",
                                    "{instrument:%} retez", None)
        )

    def test_instrument_empty_plural_format(self):
        self.assertTrue(
            self.check.check_single("{instrument:%|instruments} string",
                                    "{instrument:%|} retez", None)
        )

    def test_vocal_format(self):
        self.assertFalse(
            self.check.check_single("{vocal:%|vocals} string",
                                    "{vocal:%|nastroje} retez", None)
        )

    def test_vocal_missing_percent_format(self):
        self.assertTrue(
            self.check.check_single("{vocal:%|vocals} string",
                                    "{vocal:nastroj|nastroje} retez", None)
        )

    def test_vocal_missing_plural_format(self):
        self.assertTrue(
            self.check.check_single("{vocal:%|vocals} string",
                                    "{vocal:%} retez", None)
        )

    def test_vocal_empty_plural_format(self):
        self.assertTrue(
            self.check.check_single("{vocal:%|vocals} string",
                                    "{vocal:%|} retez", None)
        )

    def test_hyperlink_format(self):
        self.assertFalse(
            self.check.check_single("{var|title} string",
                                    "{var|titul} retez", None)
        )

    def test_text_instead_of_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{var|title} string",
                                    "{var} retez", None)
        )

    def test_empty_title_for_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{var|title} string",
                                    "{var|} retez", None)
        )

    def test_substitute_instead_of_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{var|title} string",
                                    "{var:titul} retez", None)
        )

    def test_alternative_instead_of_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{var|title} string",
                                    "{var:%|titul} retez", None)
        )

    def test_instrument_instead_of_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{instrument|title} string",
                                    "{instrument:%|titul} retez", None)
        )

    def test_vocal_instead_of_hyperlink_format(self):
        self.assertTrue(
            self.check.check_single("{vocal|title} string",
                                    "{vocal:%|titul} retez", None)
        )
