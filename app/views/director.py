from flask_restx import Namespace, Resource


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        return ''


@director_ns.route('/<int:dir>')
class DirectorView(Resource):

    def get(self, dir):
        return ''

