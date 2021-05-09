# -*- coding: utf-8 -*-
"""Notes widget views."""
import tkinter as tk
from dataclasses import dataclass
import datetime

from views.shared.scrollable import Scrollable
from views.shared.flexible import Flexible
from views.shared.view import View


@dataclass
class NoteViewProps:
    """Props for note view."""

    title: str
    text: str
    createdTime: datetime.datetime
    lastChangeTime: datetime.datetime

class CurrentNote(View[NoteViewProps]):
    """View for openeed note."""
    
    def _update(self):
        pass

    def _render_widgets(self):
        if self.props:
            self._title = Flexible(tk.Label)(self, text = self.props.title)
            self._text = Flexible(tk.Label)(self, text = self.props.text)
        else:
            self._title = Flexible(tk.Label)(self)
            self._text = Flexible(tk.Label)(self)
        self._title.grid(row = 0, column = 0, sticky = "NEWS")
        self._text.grid(row = 1, column = 0, sticky="NEWS")

class NoteHeader(View[NoteViewProps]):
    """View for note in scrollable view."""

    def _update(self):
        pass

    def _render_widgets(self):
        self._title = Flexible(tk.Label)(self, text = self.props.title)
        self._lastChangeTime = Flexible(tk.Label)(self, text = self.props.lastChangeTime)

        self._title.grid(row = 0, column = 0, sticky = "NEWS")
        self._lastChangeTime.grid(row = 1, column = 0, sticky="NEWS")

class NotesView(View):
    """View for notes screen."""

    def _update(self):
        pass

    def _render_widgets(self):
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)

        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 0)
        self.columnconfigure(2, weight = 0)
        self.columnconfigure(3, weight = 1)

        self._newButton = Flexible(tk.Button)(self, text="New")
        self._newButton.grid(column = 0, row = 0, sticky="NEWS")
        self._saveButton = Flexible(tk.Button)(self, text="Save")
        self._saveButton.grid(column = 1, row = 0, sticky="NEWS")
        self._deleteButton = Flexible(tk.Button)(self, text="Delete")
        self._deleteButton.grid(column = 2, row = 0, sticky="NEWS")
        self._notesList = Scrollable(self)
        self._notesList.grid(column = 0, row = 1, columnspan = 3, sticky="NEWS")
        self._currentNote = CurrentNote(self)
        self._currentNote.grid(column = 4, row = 0, rowspan = 2, sticky="NEWS")
