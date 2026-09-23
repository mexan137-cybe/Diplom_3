from selenium.webdriver.common.by import By

class OrderCreatedLocators:

    ORDER_NUMBER = (By.XPATH,'//p[text()="идентификатор заказа"]/preceding-sibling::h2[contains(@class, "Modal_modal__title_shadow")]')
    CLOSE_BUTTON = (By.XPATH,'//p[text()="идентификатор заказа"]/ancestor::section//button[contains(@class, "Modal_modal__close")]')