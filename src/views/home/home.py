# -*- coding: utf-8 -*-

import tkinter as tk

from views.shared.flexible.flexible import Flexible


class HomeView(Flexible(tk.LabelFrame)):
    def __init__(self, parent):
        super().__init__(parent, text='HomeView')
        self.__render()

    def __render(self):
        self.__text = Flexible(tk.Text)(
            self,
            undo=True,
            wrap=tk.WORD,
            font="fixed",
        )
