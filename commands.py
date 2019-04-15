import pytest
from app.models import Usuario, db

def test(coverage=False):
    comandos = ['-s', './app/tests', '-p', 'no:warnings']

    if coverage:
        comandos.append('--cov')

    pytest.main(comandos)


def seed():
    usuarios = [
        Usuario(nome='Leanne Graham', email='Sincere@april.biz', senha='Gwenborough'),
        Usuario(nome='Ervin Howell', email='Shanna@melissa.tv', senha='Wisokyburgh'),
        Usuario(nome='Clementine Bauch', email='Nathan@yesenia.net', senha='McKenziehaven'),
        Usuario(nome='Patricia Lebsack', email='Julianne.OConner@kory.org', senha='South Elvis'),
        Usuario(nome='Chelsey Dietrich', email='Lucio_Hettinger@annie.ca', senha='Roscoeview'),
        Usuario(nome='Mrs. Dennis Schulist', email='Karley_Dach@jasper.info', senha='South Christy'),
        Usuario(nome='Kurtis Weissnat', email='Telly.Hoeger@billy.biz', senha='Howemouth'),
        Usuario(nome='Nicholas Runolfsdottir V', email='Sherwood@rosamond.me', senha='Aliyaview'),
        Usuario(nome='Glenna Reichert', email='Chaim_McDermott@dana.io', senha='Bartholomebury'),
        Usuario(nome='Clementina DuBuque', email='Rey.Padberg@karina.biz', senha='Lebsackbury')
    ]

    for usuario in usuarios:
        print('Incluindo usuario {}'.format(usuario.nome))
        db.session.add(usuario)

    db.session.commit()
    print('Seed finnalizado.')


def drop_all():
    db.drop_all()