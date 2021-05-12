# -*- coding: utf-8 -*-
"""Scrollable area widget."""
import tkinter as tk
from sys import platform
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

    def _render(self):
        self.columnconfigure(1, minsize=8)
        self._canvas = tk.Canvas(self, confine=True)
        self._canvas.grid(row=0, column=0, sticky="NEWS")
        self._scroll = ttk.Scrollbar(
            self, orient="vertical", command=self._canvas.yview
        )
        self._scroll.grid(row=0, column=1, sticky="NEWS")

        self._canvas.configure(yscrollcommand=self._scroll.set)
        self._bind_mouse_scroll()

        self._container = ttk.Frame(self._canvas)
        self._container.grid(sticky="NEWS")
        self._container.bind("<Configure>", self._on_resize)
        self._container_id = self._canvas.create_window(
            (0, 0), window=self._container, anchor="nw"
        )

    def _bind_mouse_scroll(self):
        # Scroll is OS-dependent.
        # Read more: https://stackoverflow.com/a/17457843
        if platform == "darwin":
            # macOS
            self._canvas.bind_all(
                "<MouseWheel>", lambda e: self._canvas.yview_scroll(-e.delta, "units")
            )
        elif platform == "win32":
            # Windows
            self._canvas.bind_all(
                "<MouseWheel>",
                lambda e: self._canvas.yview_scroll(-e.delta / 120, "units"),
            )
        else:
            # Linux
            def on_scroll_up(e):
                self._canvas.yview_scroll(-1, "units")

            def on_scroll_down(e):
                self._canvas.yview_scroll(1, "units")

            self._canvas.bind_all("<Button-4>", on_scroll_up)
            self._canvas.bind_all("<Button-5>", on_scroll_down)

    def _on_resize(self, _):
        self._canvas.configure(scrollregion=self._container.bbox("all"))
