"""Calendar tab controllers."""

import datetime

from overview.models.calendar import CalendarModel
from overview.utils.dates import getFirstDayOfNextMonth, getFirstDayOfPrevMonth
from overview.views.calendar import CalendarView, CalendarViewProps


class CalendarController:
    """Calendar controller."""

    def __init__(self):
        """Construct controller."""
        self._view = None

    def createView(self, master) -> CalendarView:
        """Create view for calendar tab.

        :return: new view for calendar
        """
        self._model = CalendarModel()
        self._view = CalendarView(master)
        self._current_date = datetime.date.today()
        self._view.currentNote.bind("<Leave>", lambda e: self._saveNote())
        self._view.arrowLeft.configure(command=self._goPrevMonth)
        self._view.arrowRight.configure(command=self._goNextMonth)
        self._update_view()
        return self._view

    def _update_view(self):
        self._view.update_props(
            CalendarViewProps(self._model.notes, self._current_date, self._switchNote)
        )

    def _update_current_date(self, day: int):
        self._current_date = self._current_date.replace(day=day)
        self._view.updateCurrentDate(day)

    def _saveNote(self):
        self._model.updateNote(
            self._current_date,
            self._view.currentNote.get("1.0", "end"),
        )

    def _switchNote(self, dayNumber):
        self._saveNote()
        self._update_current_date(dayNumber)

    def _goNextMonth(self):
        self._saveNote()
        self._current_date = getFirstDayOfNextMonth(self._current_date)
        self._update_view()

    def _goPrevMonth(self):
        self._saveNote()
        self._current_date = getFirstDayOfPrevMonth(self._current_date)
        self._update_view()
