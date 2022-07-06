from pytest import fixture
from requests import Session
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json


def json_file():
    pass_file = 'pass.json'
    with open(pass_file) as json_file:
        data = json.load(json_file)
        return data


@fixture(scope='session')
def login_and_password():
    data = json_file()
    return data