import allure
import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.variables.paths import Paths
from src.variables.data import Data



@pytest.fixture(scope="function")
def get_driver(request):
    """
    Инициылизация Веб драйвера. установка параметров. Отключение лога geckodriver.log
    :param request:
    :return:
    """
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.headless = True  # False = с графическим интерфейсом, True = без графического интерфейса
    driver: WebDriver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install(),
                                         service_log_path=os.devnull)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.usefixtures("get_driver")
class TestAuthorisation2:

    def test_login(self):
        self.driver.get("https://mybank.by/main_unauthorised")
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Вход"]')))
        assert profile_element.is_displayed()
        self.driver.find_element(By.XPATH, '//span[text()="Вход"]').click()
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="phoneNumber"]')))
        assert profile_element.is_displayed()
        self.driver.find_element(By.XPATH, Paths.PHONE_INPUT).send_keys(Data.MAIN_USER['telephone'])
        # self.driver.find_element(By.XPATH, '//input[@name="phoneNumber"]').send_keys(Data.MAIN_USER['telephone'])
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//form[@class="login-form"]//button[contains(text(),"Далее")]')))
        assert profile_element.is_displayed()
        self.driver.find_element(By.XPATH, '//form[@class="login-form"]//button[contains(text(),"Далее")]').click()
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Забыли пароль?"]')))
        assert profile_element.is_displayed()
        self.driver.find_element(By.XPATH, '//span[text()="Забыли пароль?"]').click()
        profile_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Код из СМС")]/following::input[1]')))
        assert profile_element.is_displayed()
        self.driver.find_element(By.XPATH, '//label[contains(text(), "Код из СМС")]/following::input[1]').send_keys(Data.SMS)
        time.sleep(2)

    def test_login2(self):
        print("!!!!!" + Paths.PHONE_INPUT)

