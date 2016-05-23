#!/bin/python
from uuid import uuid4

from jinja2 import Environment, FileSystemLoader
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.environ.get('CONFIG_FILE_PATH', '/tryton/config.ini')
TRYTONPASS_FILE_PATH = os.environ.get('TRYTONPASSFILE', '/tryton/TRYTONPASSFILE.ini')


class FileCreater(object):
    def __init__(self):
        self.j2_env = Environment(loader=FileSystemLoader(THIS_DIR))
        self.data = None

    def generate_config(self):
        template = self.j2_env.get_template('config_template.ini')
        self.data = template.render(
            DATABASE_URI=os.environ.get('DATABASE_URI'),
            STATIC_PATH=os.environ.get('STATIC_PATH'),
        )
        self.save_file()

    def save_file(self):
        with open(CONFIG_FILE_PATH, "w") as text_file:
            text_file.write(self.data)


if __name__ == '__main__':
    fc = FileCreater()
    fc.generate_config()
    print('='*30)
    print(' Config generated:')
    print(fc.data)
    print('='*30)
