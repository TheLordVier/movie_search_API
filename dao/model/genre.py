# Импортируем библиотеку Marshmallow и её функции
from marshmallow import Schema, fields
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём модель Genre с соответствующими сущностями
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Описываем модель Genre в виде класса схемы (сериализация)
class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
