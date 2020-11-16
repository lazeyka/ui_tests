import time

import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class TestLogin:

    def test_login(self):
        driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        options = webdriver.FirefoxOptions()
        options.add_argument('ignore-certificate-errors')
        driver.get("https://10.117.223.64:8086/main_unauthorised")
        # assert "Главная неавторизованная" in driver.title

        profile_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Вход"]')))
        assert profile_element.is_displayed()
        driver.find_element(By.XPATH, '//span[text()="Вход"]').click()

        profile_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="phoneNumber"]')))
        assert profile_element.is_displayed()
        driver.find_element(By.XPATH, '//input[@name="phoneNumber"]').send_keys("297612114")
        driver.find_element(By.XPATH, '//form[@class="login-form"]//button[contains(text(),"Далее")]').click()

        profile_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name = "password"]')))
        assert profile_element.is_displayed()
        driver.find_element(By.XPATH, '//input[@name = "password"]').send_keys("Qq111111")
        driver.find_element(By.XPATH, '//button[text()="Войти"]').click()

        profile_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="user-short-name"]')))
        assert profile_element.is_displayed()

        y = 0
        tr = 0  # сколько раз пробовали
        while y != 1 and tr < 60:
            try:
                driver.find_element(By.XPATH, '//span[@class="user-short-name"]').click()
                y = 1  # как только поняли, что все ок
            except Exception:
                time.sleep(1)
                tr = tr + 1  # кол-во попыток
                print("попытка номер ", tr)
        driver.find_element(By.XPATH, '//span[@class="user-short-name"]').get_attribute('value')

        driver.close()
