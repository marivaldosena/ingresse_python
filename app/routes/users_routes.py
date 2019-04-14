from flask import Blueprint, jsonify, request
from app.models import Usuario, db

users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def get_all_users():
    usuarios = [usuario.to_json() for usuario in Usuario.query.all()]

    return jsonify({'usuarios': usuarios})


@users_bp.route('/<int:user_id>')
def get_user(user_id):
    return '{}'.format(user_id)


@users_bp.route('/', methods=['POST'])
def create_user():
    json = request.get_json()

    usuario = Usuario(nome=json.get('nome', None),
                      email=json.get('email', None),
                      senha=json.get('senha', None)
                      )

    db.session.add(usuario)
    db.session.commit()

    return jsonify(usuario.to_json()), 201

