from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class UserAnswers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_answer = db.Column(db.String(100))
    answer = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    answer = db.Column(db.String(100))

class GameSessions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(150))
    player2 = db.Column(db.String(150))
    game_session_id = db.Column(db.String(128))
    player1_score = db.Column(db.Integer)
    player2_score = db.Column(db.Integer)
    player_turn = db.Column(db.String(150))
    current_question_id = db.Column(db.Integer)