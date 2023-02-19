from flask_restx import Namespace, Resource


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):

    def get(self):
        return ''


@genre_ns.route('/<int:gir>')
class GenreView(Resource):

    def get(self, gir):
        return ''

