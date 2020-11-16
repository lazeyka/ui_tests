import pytest
from src.cases.unauthorised.login import Unauthorised


@pytest.mark.usefixtures("get_driver")
class TestLoadMainUnauthorisedPage:

    def test_load_main_unauthorised_page(self):
        self.unauthorised = Unauthorised(self.driver)
        self.unauthorised.authorisation()
