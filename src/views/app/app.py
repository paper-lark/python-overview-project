# -*- coding: utf-8 -*-

import tkinter as tk

from views.home.home import HomeView
from views.shared.flexible.flexible import Flexible


class AppView(Flexible(tk.Frame)):
    def __init__(self, parent, title: str):
        super().__init__(parent)
        self.winfo_toplevel().title(title)
        self.__render()

    def __render(self):
        self.__home = HomeView(self)
