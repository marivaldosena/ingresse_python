import pytest

from app import create_app


@pytest.yield_fixture(scope='session')
def app():
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SERVER_NAME': 'localhost'
    }

    _app = create_app(config=params)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    yield app.test_client()
