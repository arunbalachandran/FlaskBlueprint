from flask_script import Manager, Shell, Server
from flask_assets import ManageAssets
from example_module import assets_env
from example_module import app

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('shell', Shell())
manager.add_command('assets', ManageAssets(assets_env))

@manager.command
def createdb():
    from example_module.models import db
    db.create_all()

if __name__ == '__main__':
    manager.run()

