from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from app.models import db, Users, Profiles
from datetime import datetime, timezone
from sqlalchemy import text

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        print(data)
        # здесь должна быть проверка корректности введенных данных
        try:
            new_user = Users(username=data['username'], password=data['password'])
            db.session.add(new_user)
            db.session.flush()

            new_profile = Profiles(name=data['name'], surname=data['surname'],
                                   birthday=data['birthday'], city=data['city'],
                                   user_id=new_user.id)
            db.session.add(new_profile)

            db.session.commit()

            # flash("logged in successfully", "success")
            print(new_user)
            print(new_profile)

        except Exception as e:
            db.session.rollback()
            print("Ошибка добавления в БД")
            print(e)

        # flash("logged in successfully", "success")
        return redirect(url_for('main.index'))
    return render_template('register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = Users.query.filter_by(username=data['username']).first()
        if user and user.password == data['password']:
            return redirect(url_for('main.index'))
    return render_template('login.html')


@bp.route('/users', methods=['GET'])
def get_users():
    profiles = Profiles.query.all()
    return jsonify([{'name': user.name, 'surname': user.surname,
                     'birthday': user.birthday, 'city': user.city} for user in profiles])
