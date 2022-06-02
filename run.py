import subprocess

from movies import create_app, db
from movies.accounts.models import *
from movies.movies.models import *


if __name__ == '__main__':
    db.create_all(app=create_app())

    try:
        subprocess.run('./set-flask-vars-and-run.sh')
    except KeyboardInterrupt:
        print()
