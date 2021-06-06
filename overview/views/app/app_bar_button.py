# -*- coding: utf-8 -*-
"""App views."""
import tkinter as tk
from dataclasses import dataclass
from typing import Callable

from overview.views.shared.flexible import Flexible
from overview.views.shared.view import View


@dataclass
class AppBarButtonViewProps:
    """Props for :class:`AppBarButtonView`."""

    text: str
    is_active: bool
    on_click: Callable[[], None]


class AppBarButtonView(View[AppBarButtonViewProps]):
    """View for application bar button."""

    def _update(self):
        self.__btn.configure(
            state=tk.ACTIVE if self.props.is_active else tk.NORMAL,
            text=self.props.text,
            command=self.props.on_click,
        )

    def _render_widgets(self):
        self.__btn = Flexible(tk.Button)(
            master=self,
            justify=tk.CENTER,
            relief=tk.FLAT,
            overrelief=tk.FLAT,
            anchor=tk.CENTER,
            bd=0,
            highlightthickness=0,
        )
        self.__btn.grid(row=0, column=0, ipadx=4, ipady=2)
