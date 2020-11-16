from selenium.webdriver.common.by import By


class Path:

    # Unauthorised
    ENTER_BUTTON = (By.XPATH, '//span[text()="Вход"]')
    NEXT_BUTTON = (By.XPATH, '//form[@class="login-form"]//button[contains(text(),"Далее")]')
    COME_IN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    PHONE_INPUT = (By.XPATH, '//input[@name="phoneNumber"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "password"]')

    # Authorised
    SHORT_NAME_BUTTON = (By.XPATH, '//span[@class="user-short-name"]')
