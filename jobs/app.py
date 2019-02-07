import Flask
from flas.templating import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")