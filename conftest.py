from pytest import fixture
from requests import Session
from selenium import webdriver
from faker import Faker
from operations.json_operations import json_file
from operations.common_selenium_operations import click_logout_button


@fixture(scope='function')
def fake_user():
    faker = Faker()
    user_name = faker.name().replace(' ', '')
    email = faker.ascii_email()
    password = faker.password(length=10)
    yield {'email': email,
            'username': user_name,
            'password': password}


@fixture(scope='session')
def login_and_password():
    data = json_file()
    yield data


@fixture(scope='session')
def session_logged(login_and_password):
    session = Session()
    session.headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        })

    session.get(url='https://boardgamegeek.com')
    session.post(url='https://boardgamegeek.com/login/api/v1', json=login_and_password)
    yield session


@fixture(scope='function')
def browser_logged_with_requests(session_logged):
    session_id = session_logged.cookies.get('SessionID')
    bgg_password = session_logged.cookies.get('bggpassword')
    bgg_username = session_logged.cookies.get('bggusername')

    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()

    driver.get(url='https://boardgamegeek.com')

    driver.add_cookie({
        'name': 'SessionID',
        'value': session_id
    })
    driver.add_cookie({
        'name': 'bggpassword',
        'value': bgg_password
    })
    driver.add_cookie({
        'name': 'bggusername',
        'value': bgg_username
    })

    driver.refresh()

    yield driver
    click_logout_button(driver)
    driver.quit()


@fixture(scope='function')
def browser_session():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(url='https://boardgamegeek.com')
    yield driver
    driver.quit()
