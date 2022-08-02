from pytest import mark


@mark.collection
class CollectionTests:

    @mark.selenium
    def test_collection_add_and_remove_item(self, browser_logged_with_requests):
        pass
