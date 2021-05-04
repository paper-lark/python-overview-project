# -*- coding: utf-8 -*-
"""Weather widget views."""
import tkinter as tk

from views.shared.flexible.flexible import Flexible


class WeatherView(Flexible(tk.LabelFrame)):
    """View for weather screen."""

    def __init__(self, parent):
        """Construct view."""
        super().__init__(parent, text="WeatherView")
