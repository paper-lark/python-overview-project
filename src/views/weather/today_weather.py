# -*- coding: utf-8 -*-
"""Weather widget views."""

import tkinter as tk
from dataclasses import dataclass
from typing import List

import utils.formatters as fmt
from models.weather import InstantForecast
from views.shared.flexible import Flexible
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
        self._scroll.container.columnconfigure(0, weight=0)
        self._scroll.container.columnconfigure(1, weight=0)
        self._scroll.container.columnconfigure(2, weight=0)
        self._scroll.container.columnconfigure(3, weight=1)

    def _render_forecast(self, index: int, forecast: InstantForecast):
        time_lbl = Flexible(tk.Label)(
            self._scroll.container,
            anchor=tk.W,
            text=fmt.format_time(forecast.ts.time()),
        )
        time_lbl.grid(row=index, padx=2, column=0)
        kind_lbl = Flexible(tk.Label)(
            self._scroll.container,
            anchor=tk.W,
            text=fmt.format_weather_kind(forecast.kind),
        )
        kind_lbl.grid(row=index, padx=2, column=1)
        temp_lbl = Flexible(tk.Label)(
            self._scroll.container,
            anchor=tk.W,
            text=fmt.format_temperature(forecast.real_temp),
        )
        temp_lbl.grid(row=index, padx=2, column=2)
        wind_lbl = Flexible(tk.Label)(
            self._scroll.container,
            anchor=tk.W,
            text=fmt.format_wind(forecast.wind_speed, forecast.wind_direction),
        )
        wind_lbl.grid(row=index, padx=2, column=3)

        return [time_lbl, kind_lbl, temp_lbl, wind_lbl]

    def _update(self):
        for r in self.__rows:
            for e in r:
                e.destroy()
        self.__rows = [
            self._render_forecast(i, f) for i, f in enumerate(self.props.forecasts[:24])
        ]
