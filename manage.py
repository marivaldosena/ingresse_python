import commands
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app

manager = Manager(create_app)


@manager.command
def test(coverage=False):
    commands.test(coverage=coverage)


@manager.command
def seed():
    commands.seed()


@manager.command
def drop_all():
    commands.drop_all()


if __name__ == '__main__':
    manager.add_command('db', MigrateCommand)
    manager.run()
