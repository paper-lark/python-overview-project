# -*- coding: utf-8 -*-
"""Calendar widget views."""
import datetime
import tkinter as tk
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable

from utils.formatters import format_month_EN, format_month_year
from utils.utils import getNumberOfDays
from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class CalendarViewProps:
    """Props for calendar view."""

    notesDict: OrderedDict
    currentDate: datetime.date
    onClick: Callable


@dataclass
class CalendarDayButtonProps:
    """Props for calendar day button."""

    currentDay: int
    onClick: Callable


class CalendarDayButton(View[CalendarDayButtonProps]):
    """View for calendar day button."""

    def _update(self):
        self.dayButton.configure(
            text=self.props.currentDay,
            command=lambda: self.props.onClick(self.props.currentDay),
        )

    def _render_widgets(self):
        self.dayButton = Flexible(tk.Button)(self)


class CalendarView(View[CalendarViewProps]):
    """View for calendar screen."""

    def updateCurrentDate(self, day):
        """Update only day in the same month."""
        self.props.currentDate = self.props.currentDate.replace(day=day)
        self.currentNote.delete("1.0", "end")
        if self.props.currentDate in self.props.notesDict:
            self.currentNote.insert(
                "1.0", self.props.notesDict[self.props.currentDate].text[:-1]
            )

        for i, b in enumerate(self.daysButtons):
            if i == self.props.currentDate.day - 1:
                b.dayButton.configure(font="TkDefaultFont 12 bold", state=tk.DISABLED)
            elif self.props.currentDate.replace(day=i + 1) in self.props.notesDict:
                b.dayButton.configure(font="TkDefaultFont 12 bold", state=tk.NORMAL)
            else:
                b.dayButton.configure(font="TkDefaultFont 12", state=tk.NORMAL)

    def _update(self):
        for b in self.daysButtons:
            b.destroy()
        self.daysButtons = []

        self.currentMonth.configure(
            text=format_month_EN(format_month_year(self.props.currentDate))
        )

        numberOfDays = getNumberOfDays(self.props.currentDate)
        numberOfWeeks = 4
        firstDayWeekday = self.props.currentDate.replace(day=1).weekday()
        lastDayWeekday = self.props.currentDate.replace(day=numberOfDays).weekday()
        while numberOfWeeks * 7 < numberOfDays + firstDayWeekday + 6 - lastDayWeekday:
            numberOfWeeks += 1

        for i in range(numberOfWeeks):
            self.daysButtonsContainer.rowconfigure(i, weight=1)
        for j in range(7):
            self.daysButtonsContainer.columnconfigure(j, weight=1)

        for i in range(numberOfWeeks):
            for j in range(7):
                if (
                    i == 0
                    and j < firstDayWeekday
                    or i == numberOfWeeks - 1
                    and j > lastDayWeekday
                ):
                    continue
                else:
                    self.daysButtons.append(
                        CalendarDayButton(self.daysButtonsContainer)
                    )
                    self.daysButtons[-1].update_props(
                        CalendarDayButtonProps(
                            i * 7 + j - firstDayWeekday + 1, self.props.onClick
                        )
                    )
                    self.daysButtons[-1].grid(row=i, column=j, sticky="NEWS")

        self.updateCurrentDate(self.props.currentDate.day)

    def _render_widgets(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.monthChooseBar = Flexible(tk.Canvas)(self)
        self.monthChooseBar.grid(row=0, sticky="NEWS")
        self.monthChooseBar.columnconfigure(0, weight=0)
        self.monthChooseBar.columnconfigure(1, weight=1)
        self.monthChooseBar.columnconfigure(2, weight=0)

        self.arrowLeft = Flexible(tk.Button)(self.monthChooseBar, text="<")
        self.currentMonth = Flexible(tk.Label)(self.monthChooseBar)
        self.arrowRight = Flexible(tk.Button)(self.monthChooseBar, text=">")
        self.arrowLeft.grid(row=0, column=0, sticky="NEWS")
        self.currentMonth.grid(row=0, column=1, sticky="NEWS")
        self.arrowRight.grid(row=0, column=2, sticky="NEWS")

        self.daysButtonsContainer = Flexible(tk.Canvas)(self)
        self.daysButtonsContainer.grid(row=1, sticky="NEWS")
        self.daysButtons = []

        self.currentNote = Flexible(tk.Text)(self)
        self.currentNote.grid(row=2, sticky="NEWS")
