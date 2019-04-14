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
        assert isinstance(dados['usuarios'], list)

    def test_get_single_user(self, client):
        user_id = 1
        response = client.get(url_for('users.get_user', user_id=user_id))
        assert response.status_code == 200
        assert str(user_id) in str(response.data)

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
        assert json_data['nome'] == dados['nome']
        assert json_data['email'] == dados['email']
        assert json_data.get('senha') is None
