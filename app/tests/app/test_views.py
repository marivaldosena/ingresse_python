from flask import url_for


class TestView:
    def test_home_page(self, client):
        response = client.get(url_for('home'))
        assert response.status_code == 200
