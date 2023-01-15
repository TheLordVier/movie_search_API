# Импортируем фреймворк Flask и его функции
from flask import Flask
from flask_restx import Api
# Импортируем конфигурацию приложения из файла config.py
from config import Config
# Импортируем db из файла setup_db.py, чтобы создать БД с данными
from setup_db import db
# Импортируем созданные неймспейсы представлений из папки views
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config_object: Config):
    """
    Функция создания основного объекта app
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    """
    Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


# Создаём приложение с установленной конфигурацией
app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
