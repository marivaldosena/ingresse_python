from flask import url_for, request
import json


class TestView:
    headers = {
        'Content-Type': 'application/json'
    }

    def test_get_all_users(self, client):
        response = client.get(url_for('users.get_all_users'))
        dados = json.loads(response.data)
        assert response.status_code == 200
        assert isinstance(dados.get('usuarios'), list)

    def test_get_single_user(self, client):
        user_id = 1
        response = client.get(url_for('users.get_user', user_id=user_id))
        json_data = json.loads(response.data)

        assert response.status_code == 200
        assert json_data.get('id') == user_id
        assert json_data.get('nome')
        assert json_data.get('email')
        assert json_data.get('senha') is None

    def test_create_user(self, client):
        dados = {
            'nome': 'nome1',
            'email': 'email1',
            'senha': 'senha1'
        }

        response = client.post(url_for('users.create_user'),
                               headers=self.headers,
                               data=json.dumps(dados))
        json_data = json.loads(response.data)

        assert response.status_code == 201
        assert json_data.get('nome') == dados.get('nome')
        assert json_data.get('email') == dados.get('email')
        assert json_data.get('senha') is None

    def test_update_user(self, client):
        user_id = 1
        dados = {
            'nome': 'nome2',
            'email': 'email2',
            'senha': 'senha2'
        }

        response = client.put(url_for('users.update_user', user_id=user_id),
                              headers=self.headers, data=json.dumps(dados))
        json_data = json.loads(response.data)

        assert response.status_code == 200
        assert dados.get('nome') == json_data.get('nome')
        assert dados.get('email') == json_data.get('email')
        assert json_data.get('senha') is None
