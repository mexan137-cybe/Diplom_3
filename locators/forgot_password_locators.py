from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
