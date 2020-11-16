import allure
from src.actions.actions_methods import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.actions.actions_methods import Actions


class Unauthorised:
    ENTER_BUTTON = (By.XPATH, '//span[text()="Вход"]')
    NEXT_BUTTON = (By.XPATH, '//form[@class="login-form"]//button[contains(text(),"Далее")]')
    COME_IN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    PHONE_INPUT = (By.XPATH, '//input[@name="phoneNumber"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "password"]')

    NUMBER = '291111111'
    NUMBER_IN_FIELD = '(29)111-11-11'

    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(self.driver)

    @allure.step
    def open(self):
        self.driver.get("https://10.117.223.64:8086/main_unauthorised")
        return self

    @allure.step
    def enter_phone(self, user_name):
        self.driver.find_element(*self.PHONE_INPUT).clear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(user_name)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    @allure.step
    def at_page(self):
        return "Главная неавторизованная" in self.driver.title

    def authorisation(self):
        self.open()
        self.at_page()
        self.actions.click_by_element(self.ENTER_BUTTON)
        self.actions.enter_in_field(self.PHONE_INPUT, self.NUMBER)
        self.actions.compare_value_in_field(self.PHONE_INPUT, self.NUMBER_IN_FIELD)
