# Импортируем объект доступа к данным GenreDAO
from dao.genre import GenreDAO


# Создаём класс GenreService
class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, filters):
        genres = self.dao.get_all(filters)
        return genres

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)
