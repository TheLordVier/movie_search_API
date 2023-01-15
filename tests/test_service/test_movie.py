
import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Прибытие"

    def test_create(self):
        movie_d = {
            "title": "Властелин колец: Возвращение короля",
            "description": "Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца.",
            "trailer": "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
            "year": 2003,
            "rating": 9.0,
            "genre_id": 6,
            "director_id": 6
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        assert self.movie_service.delete(1) is None

    def test_update(self):
        movie_d = {
            "id": 1,
            "title": "Прибытие",
            "description": "Талантливая лингвистка изучает язык пришельцев, чтобы спасти Землю.",
            "trailer": "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
            "year": 2016,
            "rating": 8.5,
            "genre_id": 1,
            "director_id": 1
        }
        assert self.movie_service.update(movie_d) is not None
