# -*- coding: utf-8 -*-
"""Weather widget views."""

import tkinter as tk
from dataclasses import dataclass
from typing import List

from models.weather import InstantForecast
from views.shared.scrollable import Scrollable
from views.shared.view import View


@dataclass
class TodayWeatherViewProps:
    """Props for :class:`TodayWeatherView`."""

    forecasts: List[InstantForecast]


class TodayWeatherView(View[TodayWeatherViewProps]):
    """View for today weather forecast."""

    def _render_widgets(self):
        self._scroll = Scrollable(self)
        self._scroll.grid(row=0, column=0, padx=8, sticky="NEWS")
        self.__rows = []

    def _render_forecast(self, row_index, forecast: InstantForecast):
        lbl = tk.Label(
            self._scroll.container,
            anchor=tk.W,
            text=f"{forecast.ts.time()} {forecast.real_temp}℃"
            + f"({forecast.feels_like_temp}℃) | wind: "
            + f"{forecast.wind_speed} mps "
            + f"(direction: {forecast.wind_direction})",
        )
        self._scroll.container.rowconfigure(row_index, weight=1)
        lbl.grid(row=row_index, column=0, sticky="NEWS")
        return lbl

    def _update(self):
        for r in self.__rows:
            r.destroy()

        self.__rows = [
            self._render_forecast(i, f) for i, f in enumerate(self.props.forecasts[:12])
        ]
