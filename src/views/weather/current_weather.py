# -*- coding: utf-8 -*-
"""Weather widget views."""

import tkinter as tk
from typing import Callable
from dataclasses import dataclass

from models.weather import InstantForecast
from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class CurrentWeatherViewProps:
    """Props for :class:`CurrentWeatherView`."""

    forecast: InstantForecast
    on_refresh: Callable[[], None]  # FIXME: use


class CurrentWeatherView(View[CurrentWeatherViewProps]):
    """View for current weather."""

    def _update(self):
        self.__real_temp.configure(text=f"{int(self.props.forecast.real_temp)}℃")
        self.__feels_like.configure(
            text=f"({int(self.props.forecast.feels_like_temp)}℃)"
        )
        self.__weather_kind.configure(text="Sunny")  # FIXME:

    def _render_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.__real_temp = Flexible(tk.Label)(
            self,
            font=("TkDefaultFont", 24),
        )
        self.__real_temp.grid(column=0, row=0)
        self.__feels_like = Flexible(tk.Label)(
            self,
            font=("TkDefaultFont", 24),
            fg="#777777",
        )
        self.__feels_like.grid(column=1, row=0)
        self.__weather_kind = Flexible(tk.Label)(
            self,
            # anchor=tk.SW
            font=("TkDefaultFont", 20),
        )
        self.__weather_kind.grid(column=0, columnspan=2, row=1)
