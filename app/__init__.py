from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.update(config)

    @app.route('/')
    def home():
        return 'Home'
        
    return app
