from src.actions.actions_methods import *
from src.actions.actions_methods import Actions
from src.variables.data import Data
from src.variables.paths import Paths


class Login:

    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(self.driver)
        self.data = Data()
        self.path = Paths()

    @allure.step("Авторизция клиента с выключенным SMS-подтверждениеним")
    def login(self):
        """
        Авторизция клиента с выключенным SMS-подтверждениеним
        :return:
        """
        self.driver.get(Data.URL_ADDRESS)
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.ENTER_BUTTON))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.PHONE_INPUT), Data.MAIN_USER['telephone'])
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.NEXT_BUTTON))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.PASSWORD_INPUT), Data.MAIN_USER['password'])
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.COME_IN_BUTTON))
        self.actions.wait_element(xpath=Paths.SHORT_NAME_BUTTON)

    @allure.step("Разлогирование клиента")
    def logout(self):
        """
        Разлогирование клиента
        :return:
        """
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.SHORT_NAME_BUTTON))
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.EXIT_BUTTON))
        self.actions.wait_element(xpath=Paths.ENTER_BUTTON)
        self.actions.check_title(self.path.TITLE_UNAUTHORISED)

    @allure.step("Забыл пароль")
    def forgot_the_pass(self):
        """
        Авторизация клиента забывшего пароль
        :return:
        """
        self.driver.get(Data.URL_ADDRESS)
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.ENTER_BUTTON))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.PHONE_INPUT), Data.MAIN_USER['telephone'])
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.NEXT_BUTTON))
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.FORGOT_PASSWORD))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.SMS_INPUT), Data.SMS)
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.COME_IN_BUTTON))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.ID_INPUT), Data.MAIN_USER['passport'])
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.NEXT_BUTTON))
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.NEW_PASSWORD), Data.MAIN_USER['password'])
        self.actions.enter_in_field(self.actions.wait_element(xpath=Paths.NEW_PASSWORD_CONFIRMATION), Data.MAIN_USER['password'])
        self.actions.click_by_element(self.actions.wait_element(xpath=Paths.SAVE_AND_ENTER_BUTTON))
        self.actions.wait_element(xpath=Paths.SHORT_NAME_BUTTON)
