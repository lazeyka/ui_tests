class Paths:

    # Unauthorised
    TITLE_UNAUTHORISED = 'Главная неавторизованная'
    ENTER_BUTTON = '//span[text()="Вход"]'
    NEXT_BUTTON = '//form[@class="login-form"]//button[contains(text(),"Далее")]'
    COME_IN_BUTTON = '//button[text()="Войти"]'
    PHONE_INPUT = '//input[@name="phoneNumber"]'
    PASSWORD_INPUT = '//input[@name = "password"]'
    FORGOT_PASSWORD = '//span[text()="Забыли пароль?"]'
    SMS_INPUT = '//label[contains(text(), "Код из СМС")]/following::input[1]'
    ID_INPUT = '//input[@name = "personalNumber"]'
    NEW_PASSWORD = '// input[ @ name = "newPassword"]'
    NEW_PASSWORD_CONFIRMATION = '// input[ @ name = "newPassword2"]'
    SAVE_AND_ENTER_BUTTON = '//button[text()="Сохранить и войти"]'

    # Authorised
    SHORT_NAME_BUTTON = '//span[@class="user-short-name"]'
    EXIT_BUTTON = '//div[@class="header-role exit"]/span[text()="Выйти"]'
