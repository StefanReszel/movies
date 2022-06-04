from flask import Blueprint

from .views import MovieListView, MovieCreateView, MovieDetailView


movies_bp = Blueprint("movies", __name__)


movies_bp.add_url_rule('/', view_func=MovieListView.as_view('list'))
movies_bp.add_url_rule('/movie/add', view_func=MovieCreateView.as_view('create'))
movies_bp.add_url_rule('/movie/<int:id>', view_func=MovieDetailView.as_view('detail'))
