# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем экземпляр сервиса аутентификация и экземпляр юзер-сервиса
from implemented import auth_service, user_service

# Создаём неймcпейс для представлений
auth_ns = Namespace('auth')


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        """"
        Аутентификация пользователя (получение токенов)
        """
        request_json = request.json
        email = request_json.get("email", None)
        password = request_json.get("password", None)

        if None in [email, password]:
            return "Unauthorized", 401

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        """"
        Получение новых токенов по access_token и refresh_token
        """
        request_json = request.json
        access_token = request_json.get("access_token")
        refresh_token = request_json.get("refresh_token")
        validated = auth_service.validate_tokens(access_token, refresh_token)

        if not validated:
            return "Invalid token", 400

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


@auth_ns.route("/register")
class RegisterView(Resource):
    def post(self):
        """"
        Передаём email, пароль и
        создаём определённую сущность (пользователя)
        """
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if None in [email, password]:
            return "Unauthorized", 400

        user_service.create(data)
        return "The user is logged in", 201

