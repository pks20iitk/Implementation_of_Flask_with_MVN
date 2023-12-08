from flask import Flask

app =Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World how are you and your family and friends and are welcome"


@app.route("/home")
def home():
    return "Welcome to home"

from controller import*

    