from pytest import mark
from selenium.webdriver.common.by import By


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
        driver.find_element(By.CSS_SELECTOR, 'a[routerlink="/join"]').click()

        driver.find_element(By.CSS_SELECTOR, '#join-username').send_keys(fake_user['username'])
        driver.find_element(By.CSS_SELECTOR, '#join-email').send_keys(fake_user['email'])
        driver.find_element(By.CSS_SELECTOR, '#join-password').send_keys(fake_user['password'])
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        driver.find_element(By.CSS_SELECTOR, '.btn btn-lg btn-link tw-text-muted').click()
        page_source = driver.page_source

        assert 'Sign Out' in page_source



