# -*- coding: utf-8 -*-
"""Loading screen widget."""
import tkinter as tk
from tkinter import ttk

from views.shared.flexible import Flexible


class LoadingScreen(Flexible(tk.Frame)):
    """Loading screen widget."""

    def __init__(self, *args, **kwargs):
        """Construct widget."""
        super().__init__(*args, **kwargs)
        self._render()

    def start(self):
        """Start progress bar."""
        self.__loading.start()

    def stop(self):
        """Stop progress bar."""
        self.__loading.stop()

    def _render(self):
        self.rowconfigure(1, weight=1)
        self.__text = tk.Label(self, text=_("Loading…"))
        self.__text.grid(row=0, column=0, pady=16, sticky="S")
        self.__loading = ttk.Progressbar(self, mode="indeterminate")
        self.__loading.grid(row=1, column=0, padx=64, pady=16, sticky="NEW")
