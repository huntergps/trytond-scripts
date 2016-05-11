from jinja2 import Environment, FileSystemLoader
import os


# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = '/tryton/config.ini'


def generate_template():
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR))

    template = j2_env.get_template('config_template.ini')

    return template.render(
        # maps env vars to the config vars
        DATABASE_URI=os.environ.get('DATABASE_URI'),
        STATIC_PATH=os.environ.get('STATIC_PATH'),  # path for static user files
    )


def save_template(data):
    with open(CONFIG_FILE_PATH, "w") as text_file:
        text_file.write(data)


if __name__ == '__main__':
    save_template(generate_template())
