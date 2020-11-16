import time

import allure
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:
    """
        Функции для выполнения действий на странице сайта
    """
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def open(self, url):
        self.driver.get(url)
        return self

    @allure.step
    def wait_element(self, path):
        """
        Ожидаем появления элементы на странице. Передаем путь к ожидаемому элементу.
        :param path:
        :return:
        """
        profile_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                path))
        assert profile_element.is_displayed()
        return profile_element

    @allure.step
    def at_page(self):
        """
        Проверяем по title, что мы находимся на неавторизованной странице.
        :return:
        """
        assert "Главная неавторизованная" in self.driver.title

    @allure.step
    def click_by_element(self, path):
        """
        Кликаем по элементу. Передаем путь к ожидаемому элементу.
        :param path:
        :return:
        """
        y = 0
        tr = 0  # сколько раз пробовали
        self.wait_element(path)
        while y != 1 and tr < 60:
            try:
                self.wait_element(path).click()
                y = 1  # как только поняли, что все ок
            except Exception:
                time.sleep(1)
                tr = tr + 1  # кол-во попыток
                print("попытка номер ", tr)

    @allure.step
    def enter_in_field(self, path, text):
        """
        Вводит текст в поле ввода. Передаем путь к элементу и текст для ввода.
        :param path:
        :param text:
        :return:
        """
        self.wait_element(path).clear()
        try:
            self.wait_element(path).send_keys(text)
            time.sleep(2)
        except InvalidArgumentException:
            print(InvalidArgumentException)

    @allure.step
    def check_field_filled(self, path, text):
        """
        Проверяем, что в поле ввода ввели нужные символы. Передаем путь к элементу и ожидаемый текст.
        :return:
        """
        return text in self.driver.title

    @allure.step
    def compare_value_in_field(self, path, text):
        """
        Проверяем, что ввелся текст в поле ввода.
        :param path:
        :param text:
        :return:
        """
        text_element = self.wait_element(path).get_attribute('value')
        assert (text == text_element), ('Текст в поле ввода ->' + text_element + '<- не совпадает с введенным текстом '
                                                                                 '->' + text + '<-')
