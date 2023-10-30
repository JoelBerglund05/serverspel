import random
from curses import flash
from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from . import db
from .models import Questions
import sys 


def AnsweredRight():
    print("concratulations! You answered right on this question!")



gameBp = Blueprint('game', __name__)

@gameBp.route('/gamequestion', methods = ['POST', 'GET'])
@login_required
def Game():
    sql_data = Questions.query.filter_by(id=random.randint(1, 2)).first()
    return sql_data.question


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
def Error():
    return "Something went wrong!"