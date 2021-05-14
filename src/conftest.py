# -*- coding: utf-8 -*-
"""Global test configuration."""

import pytest


@pytest.fixture(scope="session", autouse=True)
def install_l10n():
    """Install localization for tests."""
    import gettext

    t = gettext.translation("messages", localedir="locale", fallback=True)
    t.install()
