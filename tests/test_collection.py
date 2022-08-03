from pytest import mark
from selenium.webdriver.common.by import By


@mark.collection
class CollectionTests:

    @mark.selenium
    def test_collection_add_and_remove_item(self, browser_logged_with_requests):
        driver = browser_logged_with_requests
        driver.find_element(By.XPATH, '//button[contains(text(), " Browse ")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(), " All Boardgames " )]').click()
        game = driver.find_element(By.CSS_SELECTOR, '#results_objectname1 > a')
        game_name = game.text
        game.click()
        driver.find_elements(By.CSS_SELECTOR, '.ng-scope > span > span > button.btn.btn-sm.btn-primary.toolbar-action-full')[1].click()
        driver.find_element(By.CSS_SELECTOR, '.modal-footer > button.btn.btn-primary').click()




