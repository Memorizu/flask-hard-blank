from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        return movie

    def create(self, data):

        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

