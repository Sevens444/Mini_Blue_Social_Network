from flask import Flask
from sqlalchemy import text
from extensions import db, login, migrate
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "777"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:0123@localhost:5432/mbsn')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    # flask db init
    # flask db migrate -m "Add messages model"
    # flask db upgrade
    login.init_app(app)

    from routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

if 1 == 2:
    with app.app_context():
        # db.session.create_all()
        result = db.session.execute(text('SELECT * FROM users'))
        print([row for row in result])

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
