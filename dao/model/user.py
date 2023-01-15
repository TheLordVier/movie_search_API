# Импортируем библиотеку Marshmallow и её функции
from marshmallow import Schema, fields
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём модель User с соответствующими сущностями
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

# Описываем модель Movie в виде класса схемы (сериализация)
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
