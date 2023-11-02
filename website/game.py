import random
from curses import flash
from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from . import db
from .models import Questions, GameSessions
import sys 
import secrets

def Game():
    sql_data = Questions.query.filter_by(id=random.randint(1, 2))
    return sql_data

gameBp = Blueprint('game', __name__)

@gameBp.route('/start-game', methods = ['POST', 'GET'])
@login_required
def StartGame():
    find_game_session = GameSessions.query.filter_by(player2="...").first()
    if find_game_session.player1 != current_user.username:
        find_game_session.player2 = current_user.username
        find_game_session.player_turn = current_user.username
        question_data = Game()
        find_game_session.current_question_id = question_data.id
        db.session.commit()
        
        return render_template('start_game.html', user=current_user, question=question)
    else:
        game_session_id = secrets.token_hex(16)
        player_name = current_user.username
        player1_score = 0
        player2_score = 0
        data = GameSessions(player1=player_name, player2="...", game_session_id=game_session_id, player1_score=player1_score, player2_score=player2_score)
        db.session.add(data)
        db.session.commit()
    return render_template('start_game.html', user=current_user)


@gameBp.route('/answer', methods = ['POST', 'GET'])
@login_required
def Answer():
    user_answer = request.form['user_answer']
    question = request.form['question']
    sql_data_question = Questions.query.filter_by(question=question).first()

    if sql_data_question.answer == user_answer:
        answer = 1
    else:
        answer = 0

    data = UserAnswers(user_answer=user_answer, answer=answer)
    db.session.add(data)
    db.session.commit()

    if answer == 1:
        return render_template('answer_right.html', user=current_user)
    
    return "hej"

@gameBp.route('/', methods = ['GET'])
def Home():
    return render_template('index.html', user=current_user)