import os
from flask import Flask

from app.extensions import (
    db,
    bcrypt,
    migrate
)

from app.routes.users_routes import users_bp


def get_config():
    env_name = os.environ.get('FLASK_ENV', 'production')

    if env_name == 'dev' or env_name == 'development':
        return 'config.development'
    elif env_name == 'test' or env_name == 'testing':
        return 'config.testing'
    else:
        return 'config.settings'


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(get_config())

    if config:
        app.config.update(config)

    app.register_blueprint(users_bp, url_prefix='/api/users')

    extensions(app)

    return app


def extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    return None
