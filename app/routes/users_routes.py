from flask import Blueprint, jsonify, request
from app.models import Usuario, db

users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def get_all_users():
    usuarios = [usuario.to_json() for usuario in Usuario.query.all()]

    return jsonify({'usuarios': usuarios}), 200


@users_bp.route('/<int:user_id>')
def get_user(user_id):
    usuario = Usuario.query.get_or_404(user_id)

    return jsonify(usuario.to_json()), 200


@users_bp.route('/', methods=['POST'])
def create_user():
    json = request.get_json()

    try:
        usuario = Usuario(nome=json.get('nome', None),
                          email=json.get('email', None),
                          senha=json.get('senha', None)
                          )

        db.session.add(usuario)
        db.session.commit()

    except AssertionError as err:
        return jsonify({'status': str(err)}), 403

    return jsonify(usuario.to_json()), 201


@users_bp.route('<int:user_id>', methods=['PUT', 'PATCH '])
def update_user(user_id):
    usuario = Usuario.query.get_or_404(user_id)

    json = request.get_json()

    usuario.nome = json.get('nome')
    usuario.email = json.get('email')
    usuario.senha = json.get('senha')

    db.session.commit()

    return jsonify(usuario.to_json()), 200


@users_bp.route('<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    usuario = Usuario.query.get_or_404(user_id)

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'status': 'Usuário excluído.'}), 204
