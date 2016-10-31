from flask import render_template, request
from . import main
from .. import db
from ..models import FilmGroup

@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route("/sys")
def sys_index():
    return render_template("sys/index.html")

@main.route("/sys/user")
def sys_user():
    return render_template("sys/user.html")

@main.route("/sys/filmgroup", methods=["GET"])
def get_filmgroups():
    """获取电影组列表"""
    fgs = FilmGroup.query.all()
    return render_template("sys/filmgroups.html", filmgroups=fgs)

@main.route("/sys/filmgroup", methods=["POST"])
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

@main.route("/sys/filmgroup/new", methods=["GET"])
def get_filmgroup_form():
    """获取电影组表单"""
    return render_template("sys/filmgroup.html")

@main.route("/sys/filmgroup/<id>", methods=["DELETE"])
def delete_filmgroup(id):
    """
    删除电影组
    id：电影组 ID
    """
    try:
        fg = FilmGroup.query.filter_by(id = id).first()
        db.session.delete(fg)
        db.session.commit()
    except Exception as e:
        print ("error msg: %s" % e)
        return "failure"

    return "success"