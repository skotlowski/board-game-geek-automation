from pytest import mark


@mark.registration
class RegisterTests:

    @mark.request
    def test_registration_user(self):
        pass

    @mark.selenium
    def test_registration_with_selenium(self):
        pass
