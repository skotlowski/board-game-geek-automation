from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_for_sign_out_button_to_be_ready(driver):
    # implicitly wait for Sign Out text or explicity wait below
    driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]')
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/logout"]')))


def click_logout_button(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]').click()


def click_all_boardgames_in_browse(driver):
    driver.find_element(By.XPATH, '//button[contains(text(), " Browse ")]').click()
    driver.find_element(By.XPATH, '//a[contains(text(), " All Boardgames " )]').click()


def click_on_first_game_from_list(driver):
    driver.find_element(By.CSS_SELECTOR, '#results_objectname1 > a')


def save_first_game_name_from_list(driver):
    return driver.find_element(By.CSS_SELECTOR, '#results_objectname1 > a').text


def save_page_source(driver):
    return driver.page_source
