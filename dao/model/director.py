# Импортируем библиотеку Marshmallow и её функции
from marshmallow import Schema, fields
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём модель Director с соответствующими сущностями
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Описываем модель Director в виде класса схемы (сериализация)
class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
