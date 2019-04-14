from flask import Blueprint, jsonify
from app.models import Usuario

users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def get_all_users():
    usuarios = Usuario.query.all()

    return jsonify({'usuarios': usuarios})


@users_bp.route('/<int:user_id>')
def get_user(user_id):
    return '{}'.format(user_id)
