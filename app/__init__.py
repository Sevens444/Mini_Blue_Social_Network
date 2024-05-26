from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from sqlalchemy import text
import os

# db = SQLAlchemy()
# migrate = Migrate()


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('app.config.Config')
#
#     db.init_app(app)
#     # migrate.init_app(app, db)
#
#     from app import routes
#     app.register_blueprint(routes.bp)
#
#     return app

app = Flask(__name__)
app.config['SECRET_KEY'] = "777"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:0123@127.0.0.1:5400/mbsn')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init_app(app)
from app import routes
app.register_blueprint(routes.bp)


if 1 == 2:
    with app.app_context():
        db.session.create_all()
        result = db.session.execute(text('SELECT * FROM users'))
        print([row for row in result])


if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)
