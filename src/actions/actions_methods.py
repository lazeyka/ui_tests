import time
import allure
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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

    @allure.step("Ожидаем появления элемента на странице.")
    def wait_element(self, text='', css='', xpath=''):
        """
        Ожидаем появления элементы на странице. Передаем путь к ожидаемому элементу.
        :param xpath: xpath=Путь к HTML Элементу на странице
        :param css: css=Путь к HTML Элементу на странице
        :param text: text=текст содержащийся в эдеиенте
        :return:
        """
        if text:
            elem = (By.XPATH, f"//*[contains(text(), '{text}')]")
        elif css:
            elem = (By.CLASS_NAME, css)
        elif xpath:
            elem = (By.XPATH, xpath)
        else:
            assert False, "Не заданы критерии поиска элемента."
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                elem))
        y = 0
        count = 0  # сколько раз пробовали кликнуть
        while y != 1 and count < 60:
            try:
                assert profile_element.is_displayed()
                y = 1  # как только поняли, что кликнули по элементу
            except Exception:
                time.sleep(1)
                count = count + 1  # кол-во попыток
                print("Ожидание появления элемента в секундах ", count)
        return profile_element

    @allure.step("Кликаем по элементу")
    def click_by_element(self, element):
        """
        Кликаем по элементу. Передаем путь к ожидаемому элементу.
        :param element: Передать элемент с которым нужно совершить действие
        :return:
        """
        y = 0
        count = 0  # сколько раз пробовали кликнуть
        while y != 1 and count < 60:
            try:
                element.click()
                y = 1  # как только поняли, что кликнули по элементу
            except Exception:
                time.sleep(1)
                count = count + 1  # кол-во попыток
                print("Попытка номер ", count)

    @allure.step("Вводим текст в поле ввода")
    def enter_in_field(self, element, text, expected_text=None):
        """
        Вводит текст в поле ввода. Передаем путь к элементу и текст для ввода.
        :param expected_text: Вводим ожидаемый текст
        :param element: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :param text: Указывает текст который необходимо ввести в проле ввода
        :return:
        """
        try:
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(text)
        except InvalidArgumentException:
            print(InvalidArgumentException)
        text_element = element.get_attribute('value')
        if expected_text is None:
            pass
        else:
            assert (expected_text == text_element), ('Текст в поле ввода -> ' + text_element +
                                                     ' <- не совпадает с введенным текстом -> ' + expected_text + ' <-')

    @allure.step("Сравниваем текст элемента с ожидаемым")
    def compare_value_in_field(self, element, expected_text):
        """
        Проверяем, что ввелся нужный текст в поле ввода.
        :param element: Путь к HTML Элементу на странице '(BY.SOMETHING, "путь")'
        :param expected_text: Текст для вода в поле
        :return:
        """
        text_element = element.get_attribute('value')
        assert (expected_text == text_element), ('Текст в поле ввода -> ' + text_element +
                                                 ' <- не совпадает с введенным текстом -> ' + expected_text + ' <-')

    @allure.step("Проверяем элемент title на нужной странице странице")
    def check_title(self, title: str):
        """
        Проверяем элемент title на странице
        :param title: title страницы
        :return:
        """
        assert title in self.driver.title
