# -*- coding: utf-8 -*-

import tkinter as tk
from dataclasses import dataclass
from typing import List, Callable

from models.app.widget_kind import WidgetKind
from views.app.app_bar_button import AppBarButtonView, AppBarButtonViewProps
from views.shared.flexible.flexible import Flexible


@dataclass
class AppBarViewProps:
    active_tab_index: int
    tabs: List[WidgetKind]
    on_activate_tab: Callable[[int], None]


class AppBarView(Flexible(tk.Frame)):
    __tab_names = {
        WidgetKind.NOTES: 'Notes',
        WidgetKind.WEATHER: 'Weather',
        WidgetKind.CALENDAR: 'Calendar'
    }  # TODO: интернационализация

    def __init__(self, parent, props: AppBarViewProps):
        super().__init__(parent)
        self.__props = props
        self.__render()

    def __render(self):
        self.grid(ipadx=4, ipady=4)
        self.__buttons = [self.__render_button(i, t) for i, t in enumerate(self.__props.tabs)]

    def __render_button(self, tab_index, tab_kind):
        btn = AppBarButtonView(
            self,
            props=AppBarButtonViewProps(
                text=self.__get_tab_name(tab_kind),
                is_active=self.__props.active_tab_index == tab_index,
                on_click=lambda: self.__props.on_activate_tab(tab_index),
            )
        )
        self.columnconfigure(tab_index, weight=1, pad=0)
        btn.grid(row=0, column=tab_index, ipadx=0, ipady=0, padx=0, pady=0)
        return btn

    @classmethod
    def __get_tab_name(cls, tab_kind):
        if tab_kind not in cls.__tab_names:
            raise Exception(f'unsupported tab kind={tab_kind}')
        return cls.__tab_names[tab_kind]