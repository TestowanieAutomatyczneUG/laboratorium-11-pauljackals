import unittest
from unittest.mock import mock_open
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


if __name__ == '__main__':
    unittest.main()
