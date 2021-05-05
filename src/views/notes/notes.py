# -*- coding: utf-8 -*-
"""Notes widget views."""
import tkinter as tk
from dataclasses import dataclass

from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class NotesViewProps:
    """Props for notes view."""

    is_loading: bool


class NotesView(View[NotesViewProps]):
    """View for notes screen."""

    def _update(self):
        pass

    def _render_widgets(self):
        self.__text = Flexible(tk.Label)(
            self,
            text="NotesView",
        )
