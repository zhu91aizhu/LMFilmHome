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

@main.route("/sys/filmgroup", methods=["GET", "POST"])
def get_filmgroups():
    """获取电影组列表"""
    if request.method == "GET":
        fgs = FilmGroup.query.all()
        return render_template("sys/filmgroups.html", filmgroups=fgs)
    else:
        ids = request.form["ids"]
        ids = ids.split(",")
        for id in ids:
            fg = FilmGroup.query.filter_by(id =id).first()
            db.session.delete(fg)
            db.session.commit()

        return "success"

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
    return render_template("sys/filmgroup.html", mod="new", fg=FilmGroup("", ""))

@main.route("/sys/filmgroup/<id>", methods=["GET", "PUT"])
def get_filmgroup(id):
    fg = FilmGroup.query.filter_by(id=id).first()

    if request.method == "GET":
        return render_template("sys/filmgroup.html", mod="browse", fg=fg)
    else:
        name = request.form["name"]
        intro = request.form["intro"]

        fg.name = name
        fg.intro = intro

        db.session.add(fg)
        db.session.commit()

        return "success"

@main.route("/sys/filmgroup/<id>/modify", methods=["GET"])
def modify_filmgroup(id):
    """
    获取电影组表单或提交电影组数据
    :param id: 电影组 ID
    :return: 返回电影组表单
    """
    fg = FilmGroup.query.filter_by(id=id).first()
    return render_template("sys/filmgroup.html", mod="modify", fg=fg)


@main.route("/sys/filmgroup/<id>", methods=["DELETE"])
def delete_filmgroup(id):
    """
    删除电影组
    :param 电影组 ID
    """
    try:
        fg = FilmGroup.query.filter_by(id = id).first()
        db.session.delete(fg)
        db.session.commit()
    except Exception as e:
        print ("error msg: %s" % e)
        return "failure"

    return "success"