from pytest import mark
from selenium_operations import register_input_username, \
    register_input_email, register_input_password, click_registration_submit_button, \
    accept_registration_form, click_join_button


@mark.registration
class RegisterTests:

    @mark.request
    def test_registration_user(self, session_logged, fake_user):
        session = session_logged
        response = session.post(url='https://boardgamegeek.com/api/accounts', json=fake_user)
        expected_response = 200

        assert response.status_code == expected_response

    @mark.selenium
    def test_registration_with_selenium(self, browser_session, fake_user):
        driver = browser_session
        click_join_button(driver)

        register_input_username(driver, fake_user)
        register_input_email(driver, fake_user)
        register_input_password(driver, fake_user)
        click_registration_submit_button(driver)

        accept_registration_form(driver)
        page_source = driver.page_source

        assert 'Sign Out' in page_source



