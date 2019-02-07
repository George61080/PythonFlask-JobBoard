import flask
from flask.templating import render_template

app = flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")