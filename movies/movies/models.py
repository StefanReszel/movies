from movies import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    added_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
