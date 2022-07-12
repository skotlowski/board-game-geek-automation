from time import sleep as wait
from requests import Session
from pytest import mark
from selenium.webdriver.common.by import By


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
        driver.find_element(By.CSS_SELECTOR, 'a[ggloginbutton=""]').click()
        driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(login_data['credentials']['username'])
        driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(login_data['credentials']['password'])
        wait(1)
        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary"]').click()
        wait(1)
        page_source = driver.page_source

        assert 'Sign Out' in page_source
