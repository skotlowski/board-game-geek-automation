from pytest import mark


@mark.registration
class RegisterTests:

    @mark.request
    def test_registration_user(self, session_logged, fake_user):
        session = session_logged
        response = session.post(url='https://boardgamegeek.com/api/accounts', json=fake_user)
        expected_response = 200

        assert response.status_code == expected_response

    @mark.selenium
    def test_registration_with_selenium(self):
        pass

