import pathlib
import os
from core.constants import constants


class File():
    def __init__(self, filename: str, content: str = None):
        self.filename = constants["BOOK_PATH"] + filename + '.md'
        self.content = content

        if self.content:
            pathlib.Path(os.path.dirname(self.filename)).mkdir(
                parents=True, exist_ok=True
            )
            self.file = open(self.filename, 'w+')

    def __del__(self):
        if self.content:
            self.file.write(self.content)
            self.file.close()
