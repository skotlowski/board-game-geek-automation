from pytest import mark
from selenium.webdriver.common.by import By
from operations.common_selenium_operations import click_all_boardgames_in_browse, click_on_first_game_from_list, \
    save_first_game_name_from_list
from operations.collection_selenium_operations import click_add_to_collection_button


@mark.collection
class CollectionTests:

    @mark.test
    def test_collection_add_and_remove_item(self, browser_logged_with_requests):
        driver = browser_logged_with_requests
        click_all_boardgames_in_browse(driver)

        game = save_first_game_name_from_list(driver)
        click_on_first_game_from_list(driver)

        click_add_to_collection_button(driver)

        # not finished yet




