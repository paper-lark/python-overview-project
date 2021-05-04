# -*- coding: utf-8 -*-
"""Home screen views."""
import tkinter as tk

from views.shared.flexible.flexible import Flexible


class HomeView(Flexible(tk.LabelFrame)):
    """View for home screen."""

    # TODO: отделить контроллер
    def __init__(self, parent):
        """Construct view."""
        super().__init__(parent, text="HomeView")
        self.__render()

    def __render(self):
        self.__text = Flexible(tk.Text)(
            self,
            undo=True,
            wrap=tk.WORD,
            font="fixed",
        )
