from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Profile, Message, db
from app import login
from datetime import datetime
import pytz
from sqlalchemy import text

bp = Blueprint('main', __name__)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/')
def index():
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        profile = Profile.query.filter_by(user_id=current_user.id).first()
        return render_template('index.html', user=user, profile=profile)
    return render_template('index.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        print(data)
        # здесь должна быть проверка корректности введенных данных
        try:
            # hashed_password = generate_password_hash(data['password'], method='sha256')
            # new_user = User(username=data['username'], password=hashed_password)
            new_user = User(username=data['username'], password=data['password'])
            db.session.add(new_user)
            db.session.flush()

            new_profile = Profile(name=data['name'], surname=data['surname'],
                                  birthday=data['birthday'], city=data['city'],
                                  user_id=new_user.id)
            db.session.add(new_profile)
            db.session.commit()
            print(new_user)
            print(new_profile)

        except Exception as e:
            db.session.rollback()
            print("Ошибка добавления в БД")
            print(e)

        return redirect(url_for('main.login'))
    return render_template('register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first()

        # if user and check_password_hash(user.password, data['password']):
        if user and user.password == data['password']:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Неправильное имя пользователя или пароль')
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/users', methods=['GET'])
def get_users():
    profiles = Profile.query.all()
    return jsonify([{'name': user.name, 'surname': user.surname,
                     'birthday': user.birthday, 'city': user.city} for user in profiles])


@bp.route('/chat', methods=['GET'])
@login_required
def chat():
    # users = User.query.all()
    users = User.query.all()
    # profiles = Profile.query.filter_by(user_id!=current_user.id).all()
    print([row for row in users])

    data = db.session.query(User, Profile).filter(User.id != current_user.id).join(Profile, User.id == Profile.user_id).all()
    return render_template('chat.html', data=data)


@bp.route('/messages/<recipient>', methods=['GET', 'POST'])
@login_required
def messages(recipient):
    recipient_user = User.query.filter_by(username=recipient).first_or_404()
    if request.method == 'POST':
        content = request.form['content']
        new_message = Message(sender_id=current_user.id, recipient_id=recipient_user.id, content=content)
        db.session.add(new_message)
        print(new_message)
        db.session.commit()
        return redirect(url_for('main.messages', recipient=recipient))
    messages_sent = Message.query.filter_by(sender_id=current_user.id, recipient_id=recipient_user.id).all()
    messages_received = Message.query.filter_by(sender_id=recipient_user.id, recipient_id=current_user.id).all()
    messages = messages_sent + messages_received
    messages.sort(key=lambda x: x.timestamp)
    return render_template('messages.html', messages=messages, recipient=recipient_user)

