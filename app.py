from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from models import FilmGroup

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/lm_film_home.db"
db = SQLAlchemy(app)

def short_intro(intro):
    if (len(intro) > 32):
        intro = intro[:32] + "..."

    return intro

def register_filter():
    env = app.jinja_env
    env.filters["short_intro"] = short_intro

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/sys")
def sys_index():
    return render_template("sys/admin-index.html")

@app.route("/sys/user")
def sys_user():
    return render_template("sys/admin-user.html")

@app.route("/sys/filmgroup", methods=["GET"])
def get_filmgroups():
    """获取电影组列表"""
    fgs = FilmGroup.query.all()
    return render_template("sys/filmgroups.html", filmgroups=fgs)

@app.route("/sys/filmgroup", methods=["POST"])
def add_filmgroup():
    """添加电影组"""
    name = request.form["name"]
    intro = request.form["intro"]

    try:
        fg = FilmGroup(name, intro)
        db.session.add(fg)
        db.session.commit()
    except Exception as e:
        print ("error msg: %s" % e)
        return "failure"

    return "success"

@app.route("/sys/filmgroup/new", methods=["GET"])
def get_filmgroup_form():
    """获取电影组表单"""
    return render_template("sys/admin-filmgroup.html")

if __name__ == "__main__":
    register_filter()
    app.run()
