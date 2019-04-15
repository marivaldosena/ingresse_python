import json
from flask import url_for, request


class TestView:
    headers = {
        'Content-Type': 'application/json'
    }

    dados_enviados = {
        'nome': 'Leanne Graham',
        'email': 'Sincere@april.biz',
        'senha': 'Gwenborough'
    }

    user_id = 1

    def test_get_all_users(self, client):
        response = client.get(
            url_for('users.get_all_users'))

        json_recebido = json.loads(response.data)

        assert response.status_code == 200
        assert isinstance(json_recebido.get('usuarios'), list)

    def test_get_single_user(self, client):
        response = client.get(
            url_for('users.get_user', user_id=self.user_id))

        json_recebido = json.loads(response.data)

        assert response.status_code == 200
        assert json_recebido.get('id') == self.user_id
        assert json_recebido.get('nome')
        assert json_recebido.get('email')
        assert json_recebido.get('senha') is None

    def test_create_user(self, client):
        dados = {
            'nome': 'Usuario 1',
            'email': 'email@email.com',
            'senha': 'senha123'
        }

        response = client.post(
            url_for('users.create_user'),
            headers=self.headers,
            data=json.dumps(dados))

        json_recebido = json.loads(response.data)

        assert response.status_code == 201
        assert json_recebido.get('nome') == dados.get('nome')
        assert json_recebido.get('email') == dados.get('email')
        assert json_recebido.get('senha') is None

    def test_create_invalid_user(self, client):
        dados = {
            'nome': 'ab',
            'email': 'email',
            'senha': '',
        }

        response = client.post(
            url_for('users.create_user'),
            headers=self.headers,
            data=json.dumps(dados)
        )

        json_recebido = json.loads(response.data)
        assert response.status_code == 403
        assert json_recebido['status'] == 'E-mail inválido.'

    def test_update_user(self, client):
        dados = {
            'nome': 'nome2',
            'email': 'email2@email.com',
            'senha': 'senha2'
        }

        response = client.put(
            url_for('users.update_user', user_id=self.user_id),
            headers=self.headers,
            data=json.dumps(dados))
        json_recebido = json.loads(response.data)

        assert response.status_code == 200
        assert dados.get('nome') == json_recebido.get('nome')
        assert dados.get('email') == json_recebido.get('email')
        assert json_recebido.get('senha') is None

    def test_delete_user(self, client):
        response = client.delete(
            url_for('users.delete_user',
                    user_id=self.user_id),
            headers=self.headers)

        assert response.status_code == 204
