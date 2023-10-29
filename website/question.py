from curses import flash
from flask import Blueprint, request
from flask_login import current_user
from . import db
from .models import Questions

questionBp = Blueprint('question', __name__)

@questionBp.route('/questionadd', methods = ['POST', 'GET'])
def Question():
    question = request.form['question']
    answer = request.form['answer']
    data = Questions(question=question, answer=answer)
    db.session.add(data)
    db.session.commit()
    return "success"