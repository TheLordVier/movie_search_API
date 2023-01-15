# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему пользователя
from dao.model.user import UserSchema
# Импортируем экземпляр сервиса пользователь
from implemented import user_service
# Импортируем декораторы доступа (auth_required и admin_required) из файла decorators.py
from decorators import auth_required

# Создаём неймcпейс для представлений
user_ns = Namespace('users')

# Cоздаём экземпляры схем
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersView(Resource):
    @auth_required
    def get(self):
        """"
        Получение списка всех сущностей (пользователь)
        """
        users = user_service.get_all()
        result = users_schema.dump(users)
        return result, 200

    @auth_required
    def post(self):
        """"
        Создание определённой сущности (пользователь)
        """
        request_json = request.json
        user = user_service.create(request_json)
        return "User created", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, uid: int):
        """"
        Получение конкретной сущности по идентификатору (пользователя)
        """
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception as e:
            return str(e), 404

    @auth_required
    def patch(self, uid: int):
        """"
        Частичное обновление конкретной сущности по идентификатору (пользователя)
        """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid
        user_service.update(request_json)
        return "User partially updated", 204

    @auth_required
    def delete(self, uid: int):
        """"
        Удаление конкретной сущности по идентификатору (пользователя)
        """
        user_service.delete(uid)
        return "User deleted", 204


@user_ns.route('/password')
class UpdateUserPasswordView(Resource):
    @auth_required
    def put(self):
        """"
        Обновление пароля пользователя
        """
        data = request.json

        email = data.get("email")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        user = user_service.get_user_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.get_password_hash(new_password)
            result = UserSchema().dump(user)
            user_service.update(result)
            print("Password updated")
        else:
            print("Password not updated")

        return "", 201
