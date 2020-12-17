import os


class FileHandler:
    def __init__(self, open_function=None, remove_function=None):
        if open_function is None:
            self.open_function = open
        else:
            self.open_function = open_function
        if remove_function is None:
            self.remove_function = os.remove
        else:
            self.remove_function = remove_function

    def read(self, path):
        try:
            with self.open_function(path) as file:
                data = file.read()
            return data
        except OSError:
            raise OSError("Can't access the file")

    def write(self, path, text):
        try:
            with self.open_function(path, 'w') as file:
                file.write(text)
            return text
        except OSError:
            raise OSError("Can't write to file")

    def remove(self, path):
        try:
            self.remove_function(path)
            return True
        except OSError:
            raise OSError("Can't remove the file")
