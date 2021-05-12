"""Notes tab controllers."""

from models.notes import NotesModel
from views.notes.notes import NotesView, NotesViewProps, NoteViewProps


class NotesController:
    """Notes controller."""

    def __init__(self):
        """Construct controller."""
        self._view = None
        self._model = NotesModel()

    def createView(self, master) -> NotesView:
        """Create view for notes tab.

        :return: new view for notes
        """
        self._view = NotesView(master)
        if len(list(self._model.notes.items())) > 0:
            self._current_id = next(reversed(self._model.notes))
        else:
            self._current_id = -1
        self._view.bind_all("<Prior>", self._goNewerNote)
        self._view.bind_all("<Next>", self._goOlderNote)
        self._view.newButton.configure(command=self._createNote)
        self._view.saveButton.configure(command=self._saveNote)
        self._view.deleteButton.configure(command=self._deleteNote)
        self._update_view()
        return self._view

    def _update_view(self):
        self._view.update_props(NotesViewProps(self._model.notes, self._current_id))
        if len(list(self._model.notes.items())) == 0:
            self._view.currentNote.disable()
        else:
            note = self._model.notes[self._current_id]
            self._view.currentNote.update_props(
                NoteViewProps(
                    note.id,
                    note.title,
                    note.text,
                    note.creationTime,
                    note.lastChangeTime,
                )
            )

    def _createNote(self):
        self._model.createNote()
        self._current_id = next(reversed(self._model.notes))
        self._update_view()

    def _saveNote(self):
        if self._view.currentNote.props:
            self._model.updateNote(
                self._view.currentNote.props.id,
                self._view.currentNote.title.get(),
                self._view.currentNote.text.get("1.0", "end"),
            )
        self._update_view()

    def _deleteNote(self):
        if self._view.currentNote.props:
            self._model.deleteNote(self._view.currentNote.props.id)
        if len(list(self._model.notes.items())) > 0:
            self._current_id = next(reversed(self._model.notes))
        self._update_view()

    def _goNewerNote(self, event):
        if len(list(self._model.notes.keys())) > 0:
            index = list(self._model.notes.keys()).index(self._current_id)
            if index < len(list(self._model.notes.keys())) - 1:
                self._current_id = list(self._model.notes.keys())[index + 1]
                self._update_view()

    def _goOlderNote(self, event):
        if len(list(self._model.notes.keys())) > 0:
            index = list(self._model.notes.keys()).index(self._current_id)
            if index > 0:
                self._current_id = list(self._model.notes.keys())[index - 1]
                self._update_view()
