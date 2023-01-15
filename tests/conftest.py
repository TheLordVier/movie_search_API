import pytest

from unittest.mock import MagicMock

from setup_db import db
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre
from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title="Прибытие",
                    description="Талантливая лингвистка изучает язык пришельцев, чтобы спасти Землю.",
                    trailer="https://www.youtube.com/watch?v=tFMo3UJ4B4g", year=2016,
                    rating=7.9, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Мементо",
                    description="Леонард ищет убийцу жены, но ему мешает амнезия.",
                    trailer="https://www.youtube.com/watch?v=4CV41hoyS8A", year=2000,
                    rating=8.4, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title="1+1",
                    description="Трогательная и глубокая комедийная драма о взаимопомощи.",
                    trailer="https://www.youtube.com/watch?v=oK5hMNxqsFA", year=2011,
                    rating=8.5, genre_id=3, director_id=3)

    movies = {
        1: movie_1,
        2: movie_2,
        3: movie_3
    }

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title="Прибытие"))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="Дени Вильнёв")
    director_2 = Director(id=2, name="Кристофер Нолан")
    director_3 = Director(id=3, name="Оливье Накаш")

    directors = {
        1: director_1,
        2: director_2,
        3: director_3
    }

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name="Фантастика")
    genre_2 = Genre(id=2, name="Драма")
    genre_3 = Genre(id=3, name="Комедия")

    genres = {
        1: genre_1,
        2: genre_2,
        3: genre_3
    }

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao
