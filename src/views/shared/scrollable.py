# -*- coding: utf-8 -*-
"""Scrollable area widget."""
import tkinter as tk
from tkinter import ttk

from views.shared.flexible import Flexible


class Scrollable(Flexible(tk.LabelFrame)):
    """Widget creates a scrollable area."""

    def __init__(self, *args, **kwargs):
        """Construct widget."""
        super().__init__(*args, **kwargs)
        self._render()

    @property
    def container(self) -> tk.Frame:
        """Container to add elements to."""
        return self._container

    def _on_mouse_scroll(self, event):
        # FIXME: use platform dependent values: https://stackoverflow.com/a/17457843
        self._canvas.yview_scroll(-event.delta, "units")

    def _on_resize(self, event):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _render(self):
        self.columnconfigure(1, minsize=8)
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0, sticky="NEWS")
        self._scroll = ttk.Scrollbar(
            self, orient="vertical", command=self._canvas.yview
        )
        self._scroll.grid(row=0, column=1, sticky="NEWS")

        self._canvas.configure(yscrollcommand=self._scroll.set)
        self._canvas.bind("<Configure>", self._on_resize)
        self._canvas.bind_all("<MouseWheel>", self._on_mouse_scroll)

        self._container = tk.Frame(self._canvas)
        self._container.grid(sticky="NEWS")
        self._container_id = self._canvas.create_window((0, 0), window=self._container, anchor="nw")
