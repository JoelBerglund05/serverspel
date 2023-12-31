from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .wsgiserver import WSGIServer

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .auth import auth
    from .game import gameBp
    from .question import questionBp


    app.register_blueprint(auth, utl_prefix='/')
    app.register_blueprint(gameBp, url_prefix='/')
    app.register_blueprint(questionBp, url_prefix='/')

    from .models import User, UserAnswers, Questions


    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'game.Home'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)