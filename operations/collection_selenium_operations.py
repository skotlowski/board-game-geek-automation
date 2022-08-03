from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_add_to_collection_button(driver):
    driver.find_elements(By.CSS_SELECTOR,
                         '.ng-scope > span > span > button.btn.btn-sm.btn-primary.toolbar-action-full')[1].click()


def click_save_to_collection_button(driver):
    driver.find_element(By.CSS_SELECTOR, '.modal-footer > button.btn.btn-primary').click()
