from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from models import FilmGroup

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/lm_film_home.db"
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/sys")
def sys_index():
    return render_template("sys/admin-index.html")

@app.route("/sys/user")
def sys_user():
    return render_template("sys/admin-user.html")

@app.route("/sys/filmgroup/new", methods=["GET"])
def sys_filmgroup():
    return render_template("sys/admin-filmgroup.html")

















@app.route("/sys/filmgroup", methods=["POST"])
def sys_add_filmgroup():
    try:
        name = request.form["filmgroup-name"]
        intro = request.form["filmgroup-intro"]

        filmgroup = FilmGroup(name, intro)
        db.session.add(filmgroup)
        db.session.submit()
        template = "sys/admin-filmgroup-add-succ.html"
    except:
        print("add filmgroup fail")
        template = "sys/admin-filmgroup-add-fail.html"

    return render_template(template)

if __name__ == '__main__':
    app.run()
