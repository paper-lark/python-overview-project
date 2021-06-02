# -*- coding: utf-8 -*-
"""App model."""
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
