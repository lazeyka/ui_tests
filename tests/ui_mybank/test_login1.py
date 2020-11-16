import time
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

search_type = 'xpath'
element_name = '//span[text()="Вход"]'


class TestLogin:

    @property
    def test_login(self):
        driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://10.117.223.64:8086/main_unauthorised")
        assert "Главная неавторизованная" in driver.title

        # profile_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//span[text()="Вход"]')))
        # assert profile_element.is_displayed()
        # driver.find_element(By.XPATH, '//span[text()="Вход"]').click()


        driver.close()
