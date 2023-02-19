from flask_restx import Namespace, Resource
from flask import request
from app.dao.model.movie import movies_schema, movie_schema
from implemented import movie_service


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieViews(Resource):

    def get(self):
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return '', 201


@movie_ns.route('/<mid>')
class MovieViews(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        movie_service.update(mid, data)
        return '', 204

    def patch(self, mid):
        data = request.json
        movie_service.update_partial(mid, data)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
