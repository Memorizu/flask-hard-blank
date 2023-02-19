from flask_restx import Namespace, Resource

from app.dao.model.director import directors_schema, director_schema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:dir>')
class DirectorView(Resource):

    def get(self, dir):
        director = director_service.get_one(dir)
        return director_schema.dump(director), 200

