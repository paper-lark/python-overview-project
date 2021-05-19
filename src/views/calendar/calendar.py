# -*- coding: utf-8 -*-
"""Calendar widget views."""
import tkinter as tk
import datetime
from collections import OrderedDict
from dataclasses import dataclass

from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class CalendarViewProps:
    """Props for calendar view."""

    notesDict: OrderedDict
    currentDate: datetime.date


class CalendarView(View[CalendarViewProps]):
    """View for calendar screen."""

    def _update(self):
        pass

    def _render_widgets(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.monthChooseBar = Flexible(tk.Canvas)(self)
        self.monthChooseBar.grid(row = 0, sticky="NEWS")
        self.monthChooseBar.columnconfigure(0, weight=0)
        self.monthChooseBar.columnconfigure(1, weight=1)
        self.monthChooseBar.columnconfigure(2, weight=0)

        self.arrowLeft = Flexible(tk.Button)(self.monthChooseBar, text = "<")
        self.currentMonth = Flexible(tk.Label)(self.monthChooseBar)
        self.arrowRight = Flexible(tk.Button)(self.monthChooseBar, text = ">")
        self.arrowLeft.grid(row = 0, column = 0, sticky="NEWS")
        self.currentMonth.grid(row = 0, column = 1, sticky="NEWS")
        self.arrowRight.grid(row = 0, column = 2, sticky="NEWS")

        self.daysButtonsContainer = Flexible(tk.Canvas)(self)
        self.daysButtonsContainer.grid(row = 1, sticky="NEWS")
        
        self.currentNote = Flexible(tk.Text)(self)
        self.currentNote.grid(row = 2, sticky="NEWS")
