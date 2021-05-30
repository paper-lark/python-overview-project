# -*- coding: utf-8 -*-
"""App model."""
import os
from dataclasses import dataclass
from enum import Enum
from sys import platform
from typing import List


class WidgetKind(Enum):
    """Supported widget kinds."""

    WEATHER = 1
    CALENDAR = 2
    NOTES = 3


@dataclass
class AppModel:
    """Model for app controller."""

    title: str
    active_tab_index: int
    tab_widgets: List[WidgetKind]


class NotesDirPath:
    """Class for holding notes path on disk."""

    _notesDirPath = os.path.join(os.path.expanduser("~"), ".Overview")
    if platform.startswith("darwin"):
        _notesDirPath = os.path.join(os.path.expanduser("~"), "Library/Overview")
    elif platform.startswith("win32"):
        _notesDirPath = os.getenv("APPDATA")
        _notesDirPath = os.path.join(_notesDirPath, "Overview")

    def getNotesDirPath() -> str:
        """Get path where notes are stored."""
        return NotesDirPath._notesDirPath
