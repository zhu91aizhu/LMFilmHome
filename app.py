from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/sys")
def sys_index():
    return render_template("sys/admin-index.html")

@app.route("/sys/user")
def sys_user():
    return render_template("sys/admin-user.html")


if __name__ == '__main__':
    app.run()
