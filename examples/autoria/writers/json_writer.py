import os
import json


class JSONWriter:
    def __init__(self, filename: str):

        self._file = open(filename, 'w', encoding='utf-8')
        self._file.write('[\n]\n')
        self._first_write = True

    def write(self, details: dict):
        self._file.seek(self._file.tell() - 2, os.SEEK_SET)

        if self._first_write:
            self._first_write = False
        else:
            self._file.write(',\n')

        json.dump(details, self._file, sort_keys=True, indent=4)
        self._file.write('\n]')
