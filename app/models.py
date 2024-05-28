from app import db
from datetime import datetime, timezone


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        # representation
        return f'Пользователь {self.username} {self.date}'

    def __str__(self):
        # representation
        return f'[ + ] Пользователь добавлен: id {self.id} {self.username} {self.password} {self.date}'


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Профиль {self.name}  {self.surname}  {self.birthday}  {self.city}"

    def __str__(self):
        return f"[ + ] Профиль: id {self.id}-{self.user_id} {self.name}  {self.surname}  {self.birthday}  {self.city}"
