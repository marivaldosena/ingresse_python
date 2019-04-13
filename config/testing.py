import os

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or \
    '331168d77efc93d6dcef1e13761890d5b764bccc74c730c3a7d743e7b6a01499'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'postgresql://username:password@hostname/test_database'
