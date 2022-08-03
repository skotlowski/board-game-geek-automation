from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_login_button(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[ggloginbutton=""]').click()


def click_sing_in_button(driver):
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary"]').click()


def login_input_username(driver, data):
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(data['credentials']['username'])


def login_input_password(driver, data):
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(data['credentials']['password'])