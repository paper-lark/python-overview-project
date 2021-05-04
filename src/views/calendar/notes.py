# -*- coding: utf-8 -*-
"""Calendar widget views."""
import tkinter as tk
from dataclasses import dataclass

from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class CalendarViewProps:
    """Props for calendar view."""

    is_loading: bool


class CalendarView(View[CalendarViewProps]):
    """View for calendar screen."""

    def _update(self):
        pass

    def _render_widgets(self):
        self.__text = Flexible(tk.Label)(
            self,
            text="CalendarView",
        )
