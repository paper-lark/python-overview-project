# -*- coding: utf-8 -*-
"""App views."""
import tkinter as tk
from dataclasses import dataclass
from typing import Callable, List

from models.app import WidgetKind
from views.app.app_bar_button import AppBarButtonView, AppBarButtonViewProps
from views.shared.view import View


@dataclass
class AppBarViewProps:
    """Props for :class:`AppBarView`."""

    active_tab_index: int
    tabs: List[WidgetKind]
    on_activate_tab: Callable[[int], None]


class AppBarView(View[AppBarViewProps]):
    """View for application bar."""

    def _update(self):
        for btn in self.__buttons:
            btn.destroy()

        self.__buttons = [
            self.__render_button(i, t) for i, t in enumerate(self.props.tabs)
        ]

    def _render_widgets(self):
        self.grid(ipadx=4, ipady=4)
        self.__buttons: List[tk.Button] = []

    def __render_button(self, tab_index, tab_kind: WidgetKind):
        self.columnconfigure(tab_index, weight=1, pad=0)
        btn = AppBarButtonView(self)
        btn.grid(row=0, column=tab_index, ipadx=0, ipady=0, padx=0, pady=0)
        btn.update_props(
            AppBarButtonViewProps(
                text=self.__get_tab_name(tab_kind),
                is_active=self.props.active_tab_index == tab_index,
                on_click=lambda: self.props.on_activate_tab(tab_index),
            )
        )
        return btn

    @classmethod
    def __get_tab_name(cls, tab_kind):
        tab_names = {
            WidgetKind.NOTES: _("Notes"),
            WidgetKind.WEATHER: _("Weather"),
            WidgetKind.CALENDAR: _("Calendar"),
        }
        if tab_kind not in tab_names:
            raise Exception(f"unsupported tab kind={tab_kind}")
        return tab_names[tab_kind]
