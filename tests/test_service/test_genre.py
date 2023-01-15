
import pytest

from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Фантастика"

    def test_create(self):
        genre_d = {
            "name": "Мюзикл"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        assert self.genre_service.delete(1) is None

    def test_update(self):
        genre_d = {
            "id": 5,
            "name": "Вестерн"
        }
        assert self.genre_service.update(genre_d) is not None
