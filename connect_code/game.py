import requests
import getpass
from .connect_server import Post



login_loop = True

while login_loop is True:
    where = input("Do you have an account? (y/n/exit): ").lower()

    password = []

    if where == "y":
        url = "login"
        username = input("Enter your username: ")
        password.append(getpass.getpass("Enter your password: "))
    elif where == "n":
        url = "sign-up"
        username = input("Enter a username: ")
        password.append(getpass.getpass("Enter a password: "))
        password.append(getpass.getpass("Enter the same password again: "))
    elif where == "exit":
        login_loop = False

    if where == "y" or where == "n":
        data = {
            'username': username,
            'password': password[0]
        }
        form_response = Post.PostData(data, url)

        if form_response.status_code == 200:
            print(form_response.text)
            login_loop = False
            game_loop = True
        else:
            print(form_response.status_code)

if game_loop is True:
    game_start = input("Would you like to start the game (y/n): ").lower()

while game_loop is True:
    if game_start == "y":
        form_response = Post.PostNoData("/")
        if form_response.status_code == 200:
            answer = input(from_response.text)