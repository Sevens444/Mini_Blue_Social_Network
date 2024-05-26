from app import db
from datetime import datetime, timezone


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f'<Users {self.username}>'


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"