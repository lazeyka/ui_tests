import allure
from src.actions.actions_methods import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.actions.actions_methods import Actions
from src.variables.data import Data
from src.variables.path_to_elements import Path


class Unauthorised:

    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(self.driver)
        self.data = Data()
        self.path = Path()


    @allure.step
    def authorisation(self):
        """
        Авторизация клиента в Итнернет Банке
        :return:
        """
        self.actions.open(self.data.URL_ADDRESS)
        self.actions.at_page()
        self.actions.click_by_element(self.path.ENTER_BUTTON)
        self.actions.enter_in_field(self.path.PHONE_INPUT, self.data.MAIN_USER['telephone'])
        self.actions.compare_value_in_field(self.path.PHONE_INPUT, self.data.MAIN_USER['telephone'])
        self.actions.click_by_element(self.path.NEXT_BUTTON)
        self.actions.enter_in_field(self.path.PASSWORD_INPUT, self.data.MAIN_USER['password'])
        self.actions.compare_value_in_field(self.path.PASSWORD_INPUT, self.data.MAIN_USER['password'])
        self.actions.click_by_element(self.path.COME_IN_BUTTON)
        self.actions.wait_element(self.path.SHORT_NAME_BUTTON)
