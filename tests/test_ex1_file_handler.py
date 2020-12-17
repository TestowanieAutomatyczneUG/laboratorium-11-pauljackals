import unittest
from unittest.mock import mock_open
from unittest.mock import Mock
from src.ex1_file.file_handler import FileHandler


class TestEx1FileHandler(unittest.TestCase):
    def test_open(self):
        text = "Open function has been mocked"
        open_function = mock_open(read_data=text)
        file_handler = FileHandler(open_function=open_function)
        self.assertEqual(file_handler.read('fake/file'), text)

    def test_write(self):
        text = "Open function has been mocked"
        open_function = mock_open()
        file_handler = FileHandler(open_function=open_function)
        self.assertEqual(file_handler.write('fake/file', text), text)

    def test_remove(self):
        remove_function = Mock(return_value=True)
        file_handler = FileHandler(remove_function=remove_function)
        self.assertTrue(file_handler.remove('fake/file'))

    def test_open_error(self):
        def no_file(x):
            if x == 'fake/nofile':
                raise OSError
        open_function = Mock(side_effect=no_file)
        file_handler = FileHandler(open_function=open_function)
        with self.assertRaisesRegex(OSError, "^Can't access the file$"):
            file_handler.read('fake/nofile')

    def test_write_error(self):
        def no_file(x, txt):
            if x == 'fake/nofile':
                raise OSError
        text = "text"
        open_function = Mock(side_effect=no_file)
        file_handler = FileHandler(open_function=open_function)
        with self.assertRaisesRegex(OSError, "^Can't write to file$"):
            file_handler.write('fake/nofile', text)

    def test_remove_error(self):
        def no_file(x):
            if x == 'fake/nofile':
                raise OSError

        remove_function = Mock(side_effect=no_file)
        file_handler = FileHandler(remove_function=remove_function)
        with self.assertRaisesRegex(OSError, "^Can't remove the file$"):
            file_handler.remove('fake/nofile')


if __name__ == '__main__':
    unittest.main()
