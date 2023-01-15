# Импортируем библиотеку Marshmallow и её функции
from marshmallow import Schema, fields
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём модель Movie с соответствующими сущностями
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(250))
    trailer = db.Column(db.String(250))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


# Описываем модель Movie в виде класса схемы (сериализация)
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
