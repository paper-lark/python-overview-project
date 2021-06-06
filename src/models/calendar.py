"""Calendar models."""
import datetime
import os
from collections import OrderedDict

from models.notes import Note
from utils.configuration import ConfigurationUtils
from utils.dates import getDatetimeFromDay, getDayMonthYear


class CalendarModel:
    """Class for managing notes with associated days."""

    def __init__(self):
        """Construct CalendarModel."""
        self._notes = OrderedDict()
        if not os.path.exists(ConfigurationUtils.getNotesDirPath()):
            os.makedirs(ConfigurationUtils.getNotesDirPath())

        for f in os.listdir(ConfigurationUtils.getNotesDirPath()):
            if f.isnumeric():
                note = Note.loadNote(f)
                try:
                    noteDate = getDatetimeFromDay(note.title)
                    self._notes[noteDate] = note
                except ValueError:
                    continue

    def createNote(self, date, text=""):
        """Create new note for given date and store it.

        :param date: date to be associated with
        :param text: text of new note
        """
        id = 0
        for i in range(len(os.listdir(ConfigurationUtils.getNotesDirPath())) + 1):
            if str(i) not in os.listdir(ConfigurationUtils.getNotesDirPath()):
                id = i
                break

        title = getDayMonthYear(date)
        self._notes[date] = Note(id, title, text)

    def deleteNote(self, date: datetime.date):
        """Delete note by date.

        :param date: date of note to be deleted
        """
        if date in self._notes.keys():
            self._notes[date].deleteFromDisk()
            del self._notes[date]

    def updateNote(self, date: datetime.date, text: str):
        """Update existing note.

        :param date: date of note to be updated
        :param text: new text of note
        """
        if date in self._notes.keys():
            if text.isspace():
                self.deleteNote(date)
            elif text != self._notes[date].text:
                self._notes[date].text = text
                self._notes.move_to_end(date)
                self._notes[date].saveNote()
        else:
            if not text.isspace():
                self.createNote(date, text)

    @property
    def notes(self):
        """Get existing notes.

        :return: OrderedDict on Note objects
        """
        return self._notes
