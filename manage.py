import pytest
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app

manager = Manager(create_app)


@manager.command
def test():
    pytest.main(['-s', 'app/tests', '-p', 'no:warnings'])
    pytest.main


if __name__ == '__main__':
    manager.add_command('db', MigrateCommand)
    manager.run()
