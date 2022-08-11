from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome_route():
    return "<h1>Welcome</h1>"
@app.route("/welcome/home")
def home_route():
    return "<h1>Welcome Home</h1>"
@app.route("/welcome/back")
def back_route():
    return "<h1>Welcome back</h1>"