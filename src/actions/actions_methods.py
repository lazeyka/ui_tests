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

    @allure.step("Открытие URL адреса")
    def open(self, url: str, title: str):
        """
        Открытие URL адреса.
        :param title: title страницы
        :param url: Адрес открываемой страницы в браузере
        :return:
        """
        self.driver.get(url)
        assert title in self.driver.title
        return self

    @allure.step("Ожидаем появления элементы на странице.")
    def wait_element(self, path: str):
        """
        Ожидаем появления элементы на странице. Передаем путь к ожидаемому элементу.
        :param path: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :return:
        """
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                path))
        assert profile_element.is_displayed()
        return profile_element

    @allure.step("Кликаем по элементу.")
    def click_by_element(self, path: str):
        """
        Кликаем по элементу. Передаем путь к ожидаемому элементу.
        :param path: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :return:
        """
        y = 0
        count = 0  # сколько раз пробовали кликнуть
        self.wait_element(path)
        while y != 1 and count < 60:
            try:
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located(
                        path)).click()
                y = 1  # как только поняли, что кликнули по элементу
            except Exception:
                time.sleep(1)
                count = count + 1  # кол-во попыток
                print("Попытка номер ", count)

    @allure.step("Вводим текст в поле ввода.")
    def enter_in_field(self, path: str, text):
        """
        Вводит текст в поле ввода. Передаем путь к элементу и текст для ввода.
        :param path: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :param text:
        :return:
        """
        self.wait_element(path).clear()
        try:
            self.wait_element(path).send_keys(text)
        except InvalidArgumentException:
            print(InvalidArgumentException)

    @allure.step("Проверяем, что ввелся нужный текст в поле ввода.")
    def compare_value_in_field(self, path: str, text):
        """
        Проверяем, что ввелся нужный текст в поле ввода.
        :param path: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :param text: Текст для вода в поле
        :return:
        """
        text_element = self.wait_element(path).get_attribute('value')
        assert (text == text_element), ('Текст в поле ввода ->' + text_element + '<- не совпадает с введенным текстом '
                                                                                 '->' + text + '<-')
