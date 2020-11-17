import allure
import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
import os


@pytest.fixture(scope="function")
def get_driver(request):
    """
    Инициылизация Веб драйвера. установка параметров. Отключение лога geckodriver.log
    :param request:
    :return:
    """
    driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), service_log_path=os.devnull)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)
