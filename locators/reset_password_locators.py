from selenium.webdriver.common.by import By

class ResetPasswordLocators:

    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    PASSWORD_SHOW_HIDE_ICON = (By.XPATH,'//label[text()="Пароль"]/following-sibling::div[contains(@class, "input__icon-action")]')
 
    