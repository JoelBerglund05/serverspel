import random
from curses import flash
from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from . import db
from .models import Questions, GameSessions
import sys 
import secrets

# TODO: Remove all debug code
# TODO: Clean up code 
# TODO: Redo bad code 

def GameSession():
    game_session_id = secrets.token_hex(16)
    player_name = current_user.username
    player1_score = 0
    player2_score = 0
    data = GameSessions(player1=player_name, player2="...", game_session_id=game_session_id, player1_score=player1_score, player2_score=player2_score)
    db.session.add(data)
    db.session.commit()

def ScoreAdder(answer_bool, game_token):
    sql_data = GameSessions.query.filter_by(game_session_id=game_token).first()
    if answer_bool == True:
        if sql_data.player_turn == sql_data.player1:
            sql_data.player1_score += 1
            sql_data.player_turn = sql_data.player2
        else:
            sql_data.player2_score += 1
            sql_data.player_turn = sql_data.player1
    elif answer_bool == False:
        if sql_data.player_turn == sql_data.player1:
            sql_data.player_turn = sql_data.player2
        else:
            sql_data.player_turn = sql_sql.player1
    db.session.commit()



def GameQuestion():
    return Questions.query.filter_by(id=random.randint(1, 2)).first()

def TryResponse(request_response):
    try:
        user_answer = request.form[request_response]
    except KeyError:
        user_answer = None
    return user_answer

def CheckAnswer(game_token, question, user_answer):
    sql_data_question = Questions.query.filter_by(question=question).first()
    print(sql_data_question.answer)
    if sql_data_question.answer == user_answer:
        answer_bool = True
        ScoreAdder(answer_bool, game_token)
        return render_template('answer_right.html', user=current_user, answer="Correct answer!", game_token=game_token)
    else:
        answer_bool = False
        return render_template('answer_right.html', user=current_user, answer="Wrong answer!", game_token=game_token)

gameBp = Blueprint('game', __name__)

@gameBp.route('/start-game', methods = ['POST', 'GET'])
@login_required
def StartGame():
    if GameSessions.query.filter_by(player2="...").first() is None:
        GameSession()
        return "loading..."
    else:
        # TODO: Rewrite this to make sence 
        try_response = TryResponse()
        find_game_session = GameSessions.query.filter_by(player2="...").first()
        if find_game_session.player1 != current_user.username and try_response is None:
            find_game_session.player2 = current_user.username
            find_game_session.player_turn = current_user.username
            question_data = GameQuestion()
            find_game_session.current_question_id = question_data.id
            db.session.commit()
            return render_template('start_game.html', user=current_user, question=question_data.question)
        elif user_answer is None:
            GameSession()
            return render_template('created_game.html', user=current_user, message="Created game! Pleas check Connect to old game to see if we have found a new game.")
        else:
            return CheckAnswer()


    return "something went wrong!"

@gameBp.route('/connect-game', methods = ['POST', 'GET'])
@login_required
def ConnectGame():
    active_games = GameSessions.query.filter_by(player2=current_user.username).all()
    active_games += GameSessions.query.filter_by(player1=current_user.username).all()
    enemy_names = []
    game_tokens = []
    for i in active_games:
        if i.player1 != current_user.username:
            enemy_names.append(i.player1)
            game_tokens.append(i.game_session_id)
        elif i.player2 != current_user.username:
            enemy_names.append(i.player2)
            game_tokens.append(i.game_session_id)

        print(game_tokens)
    if len(active_games) > 0:
        return render_template('game.html', user=current_user , active_games=enemy_names, game_tokens=game_tokens)
    else:
        return render_template('created_game.html', user=current_user, message="No active game found")

@gameBp.route('/game/<game_token>', methods = ['POST', 'GET'])
@login_required
def Game(game_token):

    # TODO: Rewrite this using if statement to check is POST

    if game_token is None:
        return "no game token!"

    user_data = [TryResponse('user_answer'), game_token, TryResponse("question")]
    print(user_data)
    game_session = GameSessions.query.filter_by(game_session_id=game_token).first()
    if game_session.player1 == current_user.username or game_session.player2 == current_user.username and game_session.player_turn == current_user.username:
        if user_data[0] == None and game_session.player_turn == current_user.username:
            question = GameQuestion()
            return render_template('game_question.html', user=current_user, question=question.question, game_token=user_data[1])
        elif user_data[0] == None:
            return "not your turn!"
        else:
            return CheckAnswer(user_data[1], user_data[2], user_data[0].lower())
    else:
        return render_template('game.html', user=current_user, active_games=game_session.player1, game_tokens=game_session.game_session_id)

@gameBp.route('/', methods = ['GET'])
def Home():
    return render_template('index.html', user=current_user)