from flask import Blueprint

users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def get_all_users():
    return 'all users'


@users_bp.route('/<int:user_id>')
def get_user(user_id):
    return '{}'.format(user_id)
