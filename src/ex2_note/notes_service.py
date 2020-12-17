from .notes_storage import NotesStorage


class NotesService:
    def __init__(self, notes_storage=None):
        self.notes_storage = notes_storage is None and NotesStorage() or notes_storage

    def add(self, note):
        return self.notes_storage.add(note)

    def average_of(self, name):
        all_notes = self.notes_storage.get_all_notes_of(name)
        if len(all_notes) == 0:
            raise ZeroDivisionError('No notes for this name')
        return sum(map(lambda note: note.get_note(), all_notes)) / len(all_notes)

    def clear(self):
        return self.notes_storage.clear()
