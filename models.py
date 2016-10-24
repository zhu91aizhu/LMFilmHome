from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase

<<<<<<< 54def5e86b738d4f59546f5adb3a1dec24091366
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/lm_film_studio.db"
db = SQLAlchemy(app)
=======
import uuid
import time

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/lm_film_home.db"
# db = SQLAlchemy(app)
db = SQLAlchemy()
>>>>>>> 功能：初始化版本

class User(AbstractConcreteBase, db.Model):

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    create_time = db.Column(db.TIMESTAMP)
    login_time = db.Column(db.TIMESTAMP)

    def __init__(self, id, username, password, create_time):
        self.id = id
        self.username = username
        self.password = password
        self.create_time = create_time

    def __repr__(self):
        return "<User username:{name}, password:{pwd}, \
            create_time:{create_time}, login_time:{login_time}>".format(
            name=self.username, pwd=self.password,
            create_time=self.create_time, login_time=self.login_time
        )

class AdminUser(User):

    __tablename__ = "admin_user"

    def __init__(self, id, username, password, create_time):
        super(AdminUser, self).__init__(id, username, password, create_time)

    def __repr__(self):
        return super().__repr__()

class GeneralUser(User):

    __tablename__ = "general_user"

    email = db.Column(db.String(255), unique=True)
    nickname = db.Column(db.String(255), unique=True)

    def __init__(self, id, username, pwd, create_time, email, nickname):
        super(GeneralUser, self).__init__(id, username, pwd, create_time)
        self.email = email
        self.nickname = nickname

    def __repr__(self):
<<<<<<< 54def5e86b738d4f59546f5adb3a1dec24091366
        return "<User username:{name}, password:{pwd}, \
=======
        return "<GeneralUser username:{name}, password:{pwd}, \
>>>>>>> 功能：初始化版本
            create_time:{create_time}, login_time:{login_time}, \
            email:{email}, nickname:{nickname}>".format(
            name=self.username, pwd=self.password,
            create_time=self.create_time, login_time=self.login_time,
            email=self.email, nickname=self.nickname
        )

<<<<<<< 54def5e86b738d4f59546f5adb3a1dec24091366
if __name__ == '__main__':
    user1 = GeneralUser("a", "user1", "user1pwd", None, "user1@lmfilmstudio.com", "user_one")
    user2 = AdminUser("b", "user2", "user2pwd", None)

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    # db.create_all()
=======
class FilmGroup(db.Model):

    __tablename__ = "filmgroups"

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    intro = db.Column(db.Text)
    create_time = db.Column(db.TIMESTAMP)
    modify_time = db.Column(db.TIMESTAMP)

    def __init__(self, name, intro):
        super(FilmGroup, self).__init__()

        self.id = uuid.uuid1()
        self.name = name
        self.intro = intro
        self.create_time = time.time()
        self.modify_time = None

    def __repr__(self):
        return "<FilmGroup id:{id}, name={name}, intro={intro}, \
            create={create}, modify={modify}".format(
            id=self.id, name=self.name, intro=self.intro,
            create=self.create_time, modify=self.modify_time
        )

if __name__ == "__main__":
    db.create_all()
>>>>>>> 功能：初始化版本
    app.run()