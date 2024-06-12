from extensions import db
from flask_login import UserMixin
from datetime import datetime
import pytz


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime(), nullable=False,
                     default=datetime.now(pytz.timezone('Europe/Moscow')))
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id',
                                    backref='sender', lazy=True)
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy=True)


    def __repr__(self):
        # representation - поля для .query
        return f'<User {self.username} {self.date.strftime("%Y.%m.%d %H:%M")}>'

    def __str__(self):
        return f'[ + ] Пользователь: id {self.id} {self.username} {self.password} {self.date}'


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Profile {self.name}  {self.surname}  {self.birthday.strftime("%Y.%m.%d")}  {self.city}>'

    def __str__(self):
        return (f'[ + ] Профиль: id {self.id} u_id {self.user_id} '
                f'{self.name} {self.surname} {self.birthday} {self.city}')


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer(), primary_key=True)
    sender_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime(), index=True,
                          default=datetime.now(pytz.timezone('Europe/Moscow')), nullable=False)

    def __repr__(self):
        return f'<Сообщение {self.content}>'

    def __str__(self):
        return (f'[ + ] Сообщение: id {self.id} s_id {self.sender_id} {self.recipient_id} '
                f'{self.content} {self.timestamp}')