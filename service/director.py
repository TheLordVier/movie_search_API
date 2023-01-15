# Импортируем объект доступа к данным DirectorDAO
from dao.director import DirectorDAO


# Создаём класс DirectorService
class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, filters):
        directors = self.dao.get_all(filters)
        return directors

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, director_d):
        self.dao.update(director_d)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)
