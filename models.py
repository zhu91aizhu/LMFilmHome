from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/lm_film_studio.db"
db = SQLAlchemy(app)

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
        return "<User username:{name}, password:{pwd}, \
            create_time:{create_time}, login_time:{login_time}, \
            email:{email}, nickname:{nickname}>".format(
            name=self.username, pwd=self.password,
            create_time=self.create_time, login_time=self.login_time,
            email=self.email, nickname=self.nickname
        )

if __name__ == '__main__':
    user1 = GeneralUser("a", "user1", "user1pwd", None, "user1@lmfilmstudio.com", "user_one")
    user2 = AdminUser("b", "user2", "user2pwd", None)

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    # db.create_all()
    app.run()