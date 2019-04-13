import os
from flask import Flask

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

    @app.route('/')
    def home():
        return 'Home'
        
    return app