# -*- coding: utf-8 -*-
"""Weather widget views."""
import tkinter as tk
from dataclasses import dataclass

from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class WeatherViewProps:
    """Props for weather view."""

    is_loading: bool


class WeatherView(View[WeatherViewProps]):
    """View for weather screen."""

    def _update(self):
        pass

    def _render_widgets(self):
        self.__text = Flexible(tk.Label)(
            self,
            text="WeatherView",
        )
