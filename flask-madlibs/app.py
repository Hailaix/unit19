from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

story = stories.story

@app.route("/")
def root_route():
    """Form page for the madlib"""
    return render_template("rootform.html", prompts=story.prompts)

@app.route("/story")
def story_route():
    """ page containing the completed madlib"""
    return render_template("storypage.html", story=story.generate(request.args))