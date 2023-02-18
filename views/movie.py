from flask_restx import Namespace, Resource
from flask import request
from dao.model.movie import Movie, movies_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieViews(Resource):

    def get(self):
        movies = Movie.query.all()
        return movies_schema.dump(movies)

    def post(self):
        req_json = request.json

        return ''