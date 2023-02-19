# файл для создания DAO и сервисов чтобы импортировать их везде
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.service.movie import MovieService
from setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

genre_dao = GenreDAO(db.session)

director_dao = DirectorDAO(db.session)
