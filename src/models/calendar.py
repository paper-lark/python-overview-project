"""Calendar models."""
import datetime
import os
from collections import OrderedDict
from sys import platform

from models.app import NotesDirPath
from models.notes import Note, NotesModel

class CalendarModel:
    """Class for managing notes with associated days."""

    def __init__(self):
        """Construct CalendarModel."""
        self._notes = OrderedDict()
        if not os.path.exists(NotesDirPath.getNotesDirPath()):
            os.makedirs(NotesDirPath.getNotesDirPath())

        for f in os.listdir(NotesDirPath.getNotesDirPath()):
            if f.isnumeric():
                note = Note.loadNote(f)
                try:
                    noteDate = datetime.date.strptime(note.title, "%d %b %Y")
                    self._notes[noteDate] = note

    def createNote(self, date, text=""):
        """Create new note for given date and store it.

        :param date: date to be associated with
        :param text: text of new note
        """
        id = 0
        for i in range(len(os.listdir(NotesDirPath.getNotesDirPath())) + 1):
            if str(i) not in os.listdir(NotesDirPath.getNotesDirPath()):
                id = i
                break

        title = date.strftime("%d %b %Y")
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
            if text == "":
                self.deleteNote(date)
            elif text != self._notes[date].text:
                self._notes[date].text = text
                self._notes.move_to_end(date)
                self._notes[date].saveNote()
        else:
            self.createNote(date, text)

    @property
    def notes(self):
        """Get existing notes.

        :return: OrderedDict on Note objects
        """
        return self._notes
