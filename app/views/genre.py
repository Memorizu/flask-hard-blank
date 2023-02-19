from flask_restx import Namespace, Resource

from app.dao.model.genre import genres_schema, genre_schema
from implemented import genre_service


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):

    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre), 200


@genre_ns.route('/<int:gir>')
class GenreView(Resource):

    def get(self, gir):
        genres = genre_service.get_one(gir)
        return genre_schema.dump(genres), 200

