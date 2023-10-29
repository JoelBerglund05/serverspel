import random
from curses import flash
from flask import Blueprint, render_template, request
from flask_login import current_user
from . import db
from .models import Questions
import sys 


def AnsweredRight():
    print("concratulations! You answered right on this question!")



gameBp = Blueprint('game', __name__)

@gameBp.route('/', methods = ['POST', 'GET'])
def Game():
    sql_data = Questions.query.filter_by(id=random.randint(1, 2)).first()
    return sql_data.question


@gameBp.route('/Upload', methods = ['POST', 'GET'])
def UploadData():
    user_answer = request.form['user_answer']
    question_id = request.form['question_id']
    user_id = request.form['user_id']
    sql_data_question = Questions.query.filter_by(id=question_id).first()

    if sql_data_question.answer == user_answer:
        answer = 1
    else:
        answer = 0

    data = UserAnswers(user_answer=user_answer, answer=answer, user_id=user_id)
    db.session.add(data)
    db.session.commit()

    if answer == 1:
        return 
    
    return "hej"

@gameBp.route('/viewdata', methods = ['GET'])
def VeiwData():
    try:
        sql_data = db.session.execute(db.select(EnviromentDetails)).scalars()
        list = ''
        for data in sql_data:
            list += (data.humidity + '% , ' + data.dateTime + ':')
        return render_template('view_data.html', list=list, user=current_user) 
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
