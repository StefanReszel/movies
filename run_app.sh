#! /bin/sh


fuser 5000/tcp --kill


export FLASK_APP=movies
export FLASK_ENV=development


python set_db.py


flask run
