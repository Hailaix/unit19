from operator import truediv
from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def index():
    session["board"] = boggle_game.make_board()
    return render_template("index.html")

@app.route("/guess", methods=["post"])
def guess_route():
    guess = request.form["guess"]
    result = boggle_game.check_valid_word(session["board"],guess)
    return jsonify({"result": result})

