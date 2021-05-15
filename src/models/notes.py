"""Notes models."""
import datetime
import os
from collections import OrderedDict
from sys import platform


class Note:
    """Class for storing note."""

    def __init__(self, id, title="Untitled", text="", savePrevious=False):
        """Construct new note model.

        :param id: unique integer - number of note
        :param title: title of note
        :param text: text of note
        :param savePrevious: True if note with this id already exists
        """
        self._id = str(id)
        self._title = title
        self._text = text
        self._creationTime = datetime.datetime.now()
        self._lastChangeTime = datetime.datetime.now()
        if not savePrevious:
            self.saveNote()

    def deleteFromDisk(self):
        """Delete note from disk."""
        os.remove(os.path.join(NotesModel.getNotesDirPath(), str(self._id)))

    def _setNote(self, title, text, creationTime, lastChangeTime):
        self._title = title
        self._text = text
        self._creationTime = creationTime
        self._lastChangeTime = lastChangeTime

    @staticmethod
    def loadNote(id: str):
        """Load note from disk.

        :param id: identifier of note (unique integer)
        :return: loaded note or empty note if loading failed
        """
        try:
            with open(os.path.join(NotesModel.getNotesDirPath(), str(id)), "r") as f:
                title = f.readline().split("\n")[0]
                creationTime = datetime.datetime.fromisoformat(
                    f.readline().split("\n")[0]
                )
                lastChangeTime = datetime.datetime.fromisoformat(
                    f.readline().split("\n")[0]
                )
                text = "".join(f.readlines())
                note = Note(id, savePrevious=True)
                note._setNote(title, text, creationTime, lastChangeTime)
                return note
        except Exception:
            return Note(id)

    def saveNote(self):
        """Save note to disk."""
        with open(os.path.join(NotesModel.getNotesDirPath(), str(self._id)), "w+") as f:
            f.write(self._title + "\n")
            f.write(self._creationTime.isoformat() + "\n")
            f.write(self._lastChangeTime.isoformat() + "\n")
            f.write(self._text)

    @property
    def id(self):
        """Get note id.

        :return: note id
        """
        return self._id

    @property
    def title(self):
        """Get note title.

        :return: note title
        """
        return self._title

    @title.setter
    def title(self, t):
        """Update note (this will change lastChangeTime).

        :param t: new note title
        """
        self._title = "".join(t.split("\n"))
        self._lastChangeTime = datetime.datetime.now()

    @property
    def text(self):
        """Get note text.

        :return: note text
        """
        return self._text

    @text.setter
    def text(self, t):
        """Update note (this will change lastChangeTime).

        :param t: new note text
        """
        self._text = t
        self._lastChangeTime = datetime.datetime.now()

    @property
    def creationTime(self):
        """Get note creation datetime.

        :return: note creation datetime
        """
        return self._creationTime

    @property
    def lastChangeTime(self):
        """Get datetime of last note change.

        :return: datetime of last note change
        """
        return self._lastChangeTime


class NotesModel:
    """Model for managing notes."""

    _notesDirPath = os.path.join(os.path.expanduser("~"), ".Overview")
    if platform.startswith("darwin"):
        _notesDirPath = os.path.join(os.path.expanduser("~"), "Library/Overview")
    elif platform.startswith("win32"):
        _notesDirPath = os.getenv("APPDATA")
        _notesDirPath = os.path.join(_notesDirPath, "Overview")

    def getNotesDirPath() -> str:
        """Get path where notes are stored."""
        return NotesModel._notesDirPath

    def __init__(self):
        """Construct NotesModel."""
        self._notes = OrderedDict()
        if not os.path.exists(NotesModel._notesDirPath):
            os.makedirs(NotesModel._notesDirPath)

        for f in os.listdir(NotesModel._notesDirPath):
            if f.isnumeric():
                self._notes[f] = Note.loadNote(f)

        self.sortNotes()

    def sortNotes(self):
        """Sort notes by datetime of last change."""
        self._notes = OrderedDict(
            sorted(self._notes.items(), key=lambda x: x[1].lastChangeTime)
        )

    def createNote(self, title="Untitled", text=""):
        """Create new note and store it.

        :param title: title of new note
        :param text: text of new note
        """
        id = 0
        for i in range(len(list(self._notes.keys())) + 1):
            if str(i) not in self._notes.keys():
                id = i
                break

        self._notes[str(id)] = Note(id, title, text)

    def deleteNote(self, id: str):
        """Delete note by id.

        :param id: id of note to be deleted
        """
        if id in self._notes.keys():
            self._notes[id].deleteFromDisk()
            del self._notes[id]

    def updateNote(self, id: str, title: str, text: str):
        """Update existing note.

        :param id: id of note to be updated
        :param title: new title of note
        :param text: new text of note
        """
        if id in self._notes.keys():
            if title != self._notes[id].title:
                self._notes[id].title = title
                self._notes.move_to_end(id)
            if text != self._notes[id].text:
                self._notes[id].text = text
                self._notes.move_to_end(id)
            self._notes[id].saveNote()

    @property
    def notes(self):
        """Get existing notes.

        :return: OrderedDict on Note objects
        """
        return self._notes
