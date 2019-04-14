from flask import url_for, request
import json


class TestView:
    def test_get_all_users(self, client):
        response = client.get(url_for('users.get_all_users'))
        dict = json.loads(response.data)
        assert response.status_code == 200
        assert isinstance((dict['usuarios']), list)

    def test_get_single_user(self, client):
        user_id = 1
        response = client.get(url_for('users.get_user', user_id=user_id))
        assert response.status_code == 200
        assert str(user_id) in str(response.data)
