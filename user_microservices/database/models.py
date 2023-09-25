from user_microservices.database.db import get_db
from werkzeug.security import generate_password_hash

db = get_db()


class USER_DATA(db.Model):

    __tablename__ = "USER_DATA"

    ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String)
    PASSWORD = db.Column(db.String)

    def __init__(self, username, password):
        self.ID = 0
        self.USERNAME = username
        self.PASSWORD = self._generate_password_hash(password)

    @staticmethod
    def _generate_password_hash(password_text):
        return generate_password_hash(password_text)
