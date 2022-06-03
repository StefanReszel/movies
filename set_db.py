from movies import create_app, db
from movies.accounts.models import *
from movies.movies.models import *


if __name__ == '__main__':
    app = create_app()
    db.create_all(app=app)
