# -*- coding: utf-8 -*-

import tkinter as tk
from dataclasses import dataclass
from typing import Callable

from views.shared.flexible.flexible import Flexible


@dataclass
class AppBarButtonViewProps:
    text: str
    is_active: bool
    on_click: Callable[[], None]


class AppBarButtonView(Flexible(tk.Frame)):
    def __init__(self, parent, props: AppBarButtonViewProps):
        super().__init__(master=parent)
        self.__props = props
        self.__render()

    def __render(self):
        self.__btn = Flexible(tk.Button)(
            master=self,
            command=self.__props.on_click,
            text=self.__props.text,
            state=tk.ACTIVE if self.__props.is_active else tk.NORMAL,
            justify=tk.CENTER,
            relief=tk.FLAT,
            overrelief=tk.FLAT,
            anchor=tk.CENTER,
            bd=0,
            highlightthickness=0
        )
        self.__btn.grid(row=0, column=0, ipadx=4, ipady=2)
