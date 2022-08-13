from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

#story = stories.story
storylist = [stories.story,stories.story2]

@app.route("/")
def root_route():
    return render_template("root.html",list=storylist)

@app.route("/form/<int:storyidx>")
def form_route(storyidx):
    """Form page for the selected story"""
    story = storylist[storyidx]
    return render_template("form.html", prompts=story.prompts, sid=storyidx)

@app.route("/story/<int:storyidx>")
def story_route(storyidx):
    story = storylist[storyidx]
    """ page containing the completed madlib"""
    return render_template("storypage.html", story=story.generate(request.args), stitle=story.title)