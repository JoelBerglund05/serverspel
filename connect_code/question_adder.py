import requests
import importlib
import connect_server

question_add = input('Add Question')
answer = input('Answer')
data = {
    'question': question_add,
    'answer': answer
    }

post_value = connect_server.Post.PostData(data, "questionadd")

if post_value.status_code == 200:
    print("successfully added")
else:
    print("error:", post_value.status_code)