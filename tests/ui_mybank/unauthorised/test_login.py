import pytest
import allure
from src.cases.unauthorised.login import Login


@allure.story('Авторизация')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("get_driver")
class TestAuthorisation:

    @allure.description('Авторизция с выключенным SMS-подтверждениеним')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.unauthorised = Login(self.driver)
        self.unauthorised.login()
