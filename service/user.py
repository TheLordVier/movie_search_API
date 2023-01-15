# Импортируем модуль base64
import base64
# Импортируем модуль hashlib для хеширования паролей
import hashlib
# Импортируем модуль hmac
import hmac

# Импортируем константы приложения(соль, количество итераций)
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
# Импортируем объект доступа к данным UserDAO
from dao.user import UserDAO


# Создаём класс UserService
class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def create(self, user_d):
        user_d["password"] = self.get_password_hash(user_d.get("password"))
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_password_hash(self, password):
        hashed_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hashed_pass)

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode("utf-8"),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )
