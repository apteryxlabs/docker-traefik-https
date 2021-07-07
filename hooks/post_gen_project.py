import os
import shutil
import subprocess

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


# Hash traefik password and add to .env:
def gen_hashed_pass(password):
    env_path = os.path.join(os.getcwd(), '.env')
    hashed = subprocess.check_output(f"openssl passwd -apr1 {password}".split())
    with open(env_path, 'a') as f:
        f.write('\nTRAEFIK_ADMIN_HASHED_PASSWORD=' + hashed.decode('utf-8').strip())


gen_hashed_pass("{{cookiecutter.TRAEFIK_ADMIN_PASSWORD}}")
