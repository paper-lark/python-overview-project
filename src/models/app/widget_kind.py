# -*- coding: utf-8 -*-
"""App models."""
from enum import Enum


class WidgetKind(Enum):
    """Supported widget kinds."""

    WEATHER = 1
    CALENDAR = 2
    NOTES = 3
