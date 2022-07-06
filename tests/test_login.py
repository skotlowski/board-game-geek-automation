from requests import Session
from pytest import mark


@mark.login
@mark.request
class LoginTests:

    def test_login(self, login_and_password):
        session = Session()
        session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            })

        expected_response = 204
        session.get(url='https://boardgamegeek.com')
        response = session.post(url='https://boardgamegeek.com/login/api/v1', json=login_and_password)
        print(response.cookies)
        assert response.status_code == expected_response
