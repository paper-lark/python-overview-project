# -*- coding: utf-8 -*-
"""App views."""
import tkinter as tk
from dataclasses import dataclass
from typing import Callable

from views.app.app_bar import AppBarView, AppBarViewProps
from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class AppViewProps:
    """Props for :class:`AppView`."""

    title: str
    app_bar: AppBarViewProps


class AppView(View[AppViewProps]):
    """View for application (root)."""

    def set_child_view(self, f: Callable[[tk.Widget], tk.Widget]):
        """Update child view, replacing old one if necessary."""
        if self.__child is not None:
            self.__child.destroy()
        self.__child = f(self.__container)
        self.__child.grid()
        return self

    def _update(self):
        self.winfo_toplevel().title(self.props.title)
        self.__bar.update_props(self.props.app_bar)

    def _render_widgets(self):
        self.__child = None
        self.rowconfigure(0, weight=0, minsize=32)
        self.rowconfigure(1, weight=1)
        self.__bar = AppBarView(self)
        self.__bar.grid(column=0, row=0)
        self.__container = Flexible(tk.Frame)(self)
        self.__container.grid(row=1, column=0, pady=8)
