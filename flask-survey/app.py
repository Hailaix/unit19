from flask import Flask, render_template, redirect, request, flash, session
from surveys import satisfaction_survey, personality_quiz, surveys
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/")
def root_route():
    """survey select page"""
    return render_template("surveyselect.html",s=surveys)

@app.route("/survey/<select>")
def survey_selected(select):
    """description page of the selected survey"""
    if surveys.get(select):
        session["survey"] = select
        return render_template("root.html",survey=surveys[session["survey"]])
    else:
        return redirect("/")
    # return render_template("root.html",survey=satisfaction_survey)

@app.route("/surveystart", methods=["POST"])
def start_survey():
    """initialize the session's responses"""
    session["responses"] = []
    return redirect(f"/question/0")

@app.route("/question/<int:num>")
def question_route(num):
    """Individual questions of the survey"""
    survey_resps = session.get("responses",[])
    if len(survey_resps) < len(surveys[session["survey"]].questions):
        if num == len(survey_resps):
            question = surveys[session["survey"]].questions[num]
            return render_template("question.html",q=question,i=num)
        else:
            flash("Invalid Question", "error")
            return redirect(f"/question/{len(survey_resps)}")
    else:
        return redirect("/thanks")

@app.route("/answer", methods=["POST"])
def answer_route():
    """add the answer to the responses"""
    survey_resps = session.get("responses",[])
    res_tup = (request.form["choice"],request.form.get("comment",""))
    survey_resps.append(res_tup)
    session["responses"] = survey_resps
    return redirect(f"/question/{len(survey_resps)}")

@app.route("/thanks")
def thanks_route():
    """Thank you page once a survey is completed"""
    return render_template("thanks.html",s=surveys[session["survey"]])
