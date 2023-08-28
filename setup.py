# Copyright © MetaBrainz Foundation
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup

setup(
    name="Weblate MusicBrainz I18n Format Check",
    version="0.1a1",
    author="yvanzo",
    author_email="yvanzo@metabrainz.org",
    description="Weblate check for MusicBrainz internationalization format.",
    install_requires=["Weblate"],
    license="GPLv3+",
    packages=["weblate_musicbrainz_format_check"],
    url=["https://musicbrainz.org/doc/MusicBrainz_Server/Internationalization#Variables"],
)
