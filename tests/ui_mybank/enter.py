import pytest
from src.pages.unauthorised.unauthorised import Unauthorised
from src.actions.actions_methods import Actions


@pytest.mark.usefixtures("get_driver")
class TestLoadMainUnauthorisedPage:

    def test_load_main_unauthorised_page(self):
        self.unauthorised = Unauthorised(self.driver)
        self.unauthorised.authorisation()
