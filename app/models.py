import re
from flask_sqlalchemy import event
from sqlalchemy.orm import validates
from app.extensions import db, bcrypt


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(70), nullable=False)
    senha = db.Column(db.String(120), nullable=False)

    def __str__(self):
        return '{}'.format(self.to_json())

    def __repr__(self):
        return '{}'.format(self.to_json())

    def to_json(self):
        json = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
        }

        return json

    @validates('email')
    def validate_email(self, key, email):
        pattern = re.compile('^\S{1,}@\S{2,}\.\S{2,}$')

        if not pattern.search(email):
            raise AssertionError('E-mail inválido.')

        e_existente = Usuario.query.filter_by(email=email).first()

        if e_existente:
            raise AssertionError('E-mail já utilizado.')

        return email


@event.listens_for(Usuario, 'before_insert')
def on_before_insert_usuario(mapper, connection, target):
    target.senha = bcrypt.generate_password_hash(target.senha).decode('utf-8')
