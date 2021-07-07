import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_db = '{{cookiecutter.use_mongo}}' == 'YES'

if not create_db:
    db_path = os.path.join(os.getcwd(), '{{cookiecutter.pkg_name}}', 'database.py')
    remove(db_path)