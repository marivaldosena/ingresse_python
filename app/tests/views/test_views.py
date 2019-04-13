from flask import url_for


class TestView:
    def test_get_all_users(self, client):
        response = client.get(url_for('users.get_all_users'))
        assert response.status_code == 200
        assert b'all users' in response.data

    def test_get_single_user(self, client):
        user_id = 1
        response = client.get(url_for('users.get_user', user_id=user_id))
        assert response.status_code == 200
        assert str(user_id) in str(response.data)