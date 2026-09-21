from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Восстановить пароль')
    CONSTRUCTOR = (By.XPATH, '//a[.//p[text()="Конструктор"]]')
    ORDERS = (By.XPATH, '//a[.//p[text()="Лента Заказов"]]')