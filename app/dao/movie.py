from app.dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self, movies):

        return movies

    def get_one(self, mid):

        movie = self.session.query(Movie).get(mid)
        return movie

    def create(self, data):

        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

