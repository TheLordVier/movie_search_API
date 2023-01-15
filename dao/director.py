# Импортируем модель Director
from dao.model.director import Director
# Импортируем конфигурацию приложения из файла config.py
from config import Config


# Создаём класс DirectorDAO
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, filter):

        page = filter.get("page")

        if page is not None:
            result = self.session.query(Director). \
                paginate(int(page), Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
