import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import FilmGroup, GeneralUser, AdminUser

app = create_app(os.getenv('FLASK_CONFIG') or "default")
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_content():
    return dict(app=app, db=db, FilmGroup=FilmGroup, GeneralUser=GeneralUser, AdminUser=AdminUser)

manager.add_command("shell", Shell(make_context=make_shell_content))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
