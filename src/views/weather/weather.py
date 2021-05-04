# -*- coding: utf-8 -*-

import tkinter as tk

from views.shared.flexible.flexible import Flexible


class WeatherView(Flexible(tk.LabelFrame)):
    def __init__(self, parent):
        super().__init__(parent, text='WeatherView')
