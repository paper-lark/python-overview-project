# -*- coding: utf-8 -*-
"""App models."""
from dataclasses import dataclass
from typing import List

from models.app.widget_kind import WidgetKind


@dataclass
class AppModel:
    """Model for app controller."""

    title: str
    active_tab_index: int
    tab_widgets: List[WidgetKind]
