from pytest import mark
from requests import Session
from selenium_operations import click_login_button, click_sing_in_button,\
    input_username, input_password, \
    check_for_sign_out_button_to_be_ready, save_page_source


@mark.login
class LoginTests:

    @mark.request
    def test_login(self, login_and_password):
        session = Session()
        session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            })

        expected_response = 204
        session.get(url='https://boardgamegeek.com')
        response = session.post(url='https://boardgamegeek.com/login/api/v1', json=login_and_password)

        assert response.status_code == expected_response

    @mark.selenium
    def test_login_with_selenium(self, login_and_password, browser_session):
        login_data = login_and_password
        driver = browser_session

        click_login_button(driver)
        input_username(driver, login_data)
        input_password(driver, login_data)
        click_sing_in_button(driver)
        check_for_sign_out_button_to_be_ready(driver)

        page_source = save_page_source(driver)

        assert 'Sign Out' in page_source
