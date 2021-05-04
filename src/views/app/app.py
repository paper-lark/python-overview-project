# -*- coding: utf-8 -*-

import tkinter as tk
from dataclasses import dataclass

from views.app.app_bar import AppBarViewProps, AppBarView
from views.home.home import HomeView
from views.shared.flexible.flexible import Flexible

@dataclass
class AppViewProps:
    title: str
    app_bar: AppBarViewProps


class AppView(Flexible(tk.Frame)):
    def __init__(self, parent, props: AppViewProps):
        super().__init__(parent)
        self.__props = props
        self.__render()

    def __render(self):
        self.winfo_toplevel().title(self.__props.title)
        self.rowconfigure(0, weight=0, minsize=32)
        self.rowconfigure(1, weight=1)

        self.__bar = AppBarView(self, self.__props.app_bar)
        self.__bar.grid(column=0, row=0)
        self.__home = HomeView(self)
        self.__home.grid(column=0, row=1, pady=8)
