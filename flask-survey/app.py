from flask import Flask, render_template
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

survey_resps = []

@app.route("/")
def root_route():
    return render_template("root.html",survey=satisfaction_survey)