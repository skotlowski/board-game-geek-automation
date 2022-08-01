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


def register_input_username(driver, fake_user):
    driver.find_element(By.CSS_SELECTOR, '#join-username').send_keys(fake_user['username'])


def register_input_email(driver, fake_user):
    driver.find_element(By.CSS_SELECTOR, '#join-email').send_keys(fake_user['email'])


def register_input_password(driver, fake_user):
    driver.find_element(By.CSS_SELECTOR, '#join-password').send_keys(fake_user['password'])


def click_registration_submit_button(driver):
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


def click_join_button(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[routerlink="/join"]').click()


def accept_registration_form(driver):
    driver.find_element(By.CSS_SELECTOR, '.btn-link').click()


def check_for_sign_out_button_to_be_ready(driver):
    # implicitly wait for Sign Out text or explicity wait below
    driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]')
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/logout"]')))


def save_page_source(driver):
    return driver.page_source
