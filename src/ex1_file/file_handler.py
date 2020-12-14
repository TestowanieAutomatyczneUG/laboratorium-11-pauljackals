class FileHandler:
    def __init__(self, open_function=None):
        if open_function is None:
            self.open_function = open
        else:
            self.open_function = open_function

    def read(self, path):
        with self.open_function(path) as file:
            data = file.read()
        return data

    def write(self, path, text):
        with self.open_function(path, 'w') as file:
            file.write(text)
        return text
