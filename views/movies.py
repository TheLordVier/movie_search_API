# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему фильма
from dao.model.movie import MovieSchema
# Импортируем экземпляр сервиса фильм
from implemented import movie_service
# Импортируем декораторы доступа (auth_required и admin_required) из файла decorators.py
from decorators import auth_required

# Создаём неймcпейс для представлений
movie_ns = Namespace('movies')

# Cоздаём экземпляры схем
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """"
        Получение списка всех сущностей (фильма)
        """
        status = request.args.get("status")
        page = request.args.get("page")

        filters = {
            "status": status,
            "page": page,
        }
        movies = movie_service.get_all(filters)
        result = movies_schema.dump(movies)
        return result, 200

    @auth_required
    def post(self):
        """"
        Создание определённой сущности (фильма)
        """
        request_json = request.json
        movie = movie_service.create(request_json)
        return "Movie created", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    @auth_required
    def get(self, mid: int):
        """"
        Получение конкретной сущности по идентификатору (фильма)
        """
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    @auth_required
    def put(self, mid: int):
        """"
        Обновление конкретной сущности по идентификатору (фильма)
        """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = mid
        movie_service.update(request_json)
        return "Movie updated", 204

    @auth_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "Movie deleted", 204
