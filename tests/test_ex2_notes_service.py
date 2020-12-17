import unittest
from unittest.mock import *
from src.ex2_note.notes_storage import NotesStorage
from src.ex2_note.notes_service import NotesService
from src.ex2_note.note import Note


class TestNotesService(unittest.TestCase):
    def setUp(self):
        def create_note(name, note):
            note_new = Note()
            note_new.get_name = MagicMock()
            note_new.get_name.return_value = name
            note_new.get_note = MagicMock()
            note_new.get_note.return_value = note
            return note_new

        self.create_note = create_note

    def test_average_of(self):
        notes_storage = NotesStorage()

        notes_storage.get_all_notes_of = MagicMock()
        notes_storage.get_all_notes_of.side_effect = (
            lambda name: name == 'Jack'
            and [self.create_note('Jack', 5.0), self.create_note('Jack', 3.0), self.create_note('Jack', 5.5)]
        )

        notes_service = NotesService(notes_storage)
        self.assertEqual(notes_service.average_of('Jack'), 4.5)

    def test_average_of_no_notes(self):
        notes_storage = NotesStorage()
        notes_storage.get_all_notes_of = MagicMock()
        notes_storage.get_all_notes_of.return_value = []

        notes_service = NotesService(notes_storage)
        with self.assertRaisesRegex(ZeroDivisionError, '^No notes for this name$'):
            notes_service.average_of('John')

    def test_add(self):
        notes_storage = NotesStorage()
        notes_storage.add = MagicMock()
        notes_storage.add.side_effect = (lambda note: note)

        notes_service = NotesService(notes_storage)
        self.assertIsInstance(notes_service.add(self.create_note('George', 5.0)), Note)

    def test_add_wrong_type(self):
        def check_note(note):
            if not isinstance(note, Note):
                raise TypeError('Note must be a Note object')

        notes_storage = NotesStorage()
        notes_storage.add = MagicMock()
        notes_storage.add.side_effect = check_note

        notes_service = NotesService(notes_storage)
        with self.assertRaisesRegex(TypeError, '^Note must be a Note object$'):
            notes_service.add(6.0)

    def test_clear(self):
        notes = [self.create_note('Jack', 5.0), self.create_note('Jack', 3.0), self.create_note('Jack', 5.5)]

        notes_storage = NotesStorage()
        notes_storage.clear = MagicMock()
        notes_storage.clear.return_value = notes

        notes_service = NotesService(notes_storage)
        self.assertListEqual(notes_service.clear(), notes)

    def tearDown(self):
        self.create_note = None


if __name__ == '__main__':
    unittest.main()
