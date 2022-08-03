from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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