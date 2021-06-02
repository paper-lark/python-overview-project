# -*- coding: utf-8 -*-
"""Classes with program configuration."""
import os
from sys import platform

class ConfigurationUtils:
    """Class for holding program configuration e.g. notes path on disk."""

    _notesDirPath = os.path.join(os.path.expanduser("~"), ".Overview")
    if platform.startswith("darwin"):
        _notesDirPath = os.path.join(os.path.expanduser("~"), "Library/Overview")
    elif platform.startswith("win32"):
        _notesDirPath = os.getenv("APPDATA")
        _notesDirPath = os.path.join(_notesDirPath, "Overview")

    def getNotesDirPath() -> str:
        """Get path where notes are stored."""
        return NotesDirPath._notesDirPath
