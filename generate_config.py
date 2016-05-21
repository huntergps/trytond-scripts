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

    def generate_config(self):
        template = self.j2_env.get_template('config_template.ini')
        config = template.render(
            DATABASE_URI=os.environ.get('DATABASE_URI'),
            STATIC_PATH=os.environ.get('STATIC_PATH'),
        )
        self.save_file(config, CONFIG_FILE_PATH)

    @staticmethod
    def save_file(data, file_path):
        with open(file_path, "w") as text_file:
            text_file.write(data)


if __name__ == '__main__':
    fc = FileCreater()
    fc.generate_config()
