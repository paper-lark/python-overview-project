# -*- coding: utf-8 -*-
"""App views."""
from dataclasses import dataclass
from typing import Optional

from views.app.app_bar import AppBarView, AppBarViewProps
from views.shared.view import View


@dataclass
class AppViewProps:
    """Props for :class:`AppView`."""

    title: str
    child_view: Optional[View]
    app_bar: AppBarViewProps


class AppView(View[AppViewProps]):
    """View for application (root)."""

    def _update(self):
        self.winfo_toplevel().title(self.props.title)
        self.__bar.update_props(self.props.app_bar)
        if self.props.child_view is not None:
            self.props.child_view.master = self
            self.props.child_view.grid(column=0, row=1, pady=8)

    def _render_widgets(self):
        self.rowconfigure(0, weight=0, minsize=32)
        self.rowconfigure(1, weight=1)
        self.__bar = AppBarView(self)
        self.__bar.grid(column=0, row=0)
