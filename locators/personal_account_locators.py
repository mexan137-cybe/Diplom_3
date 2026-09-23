from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PROFILE_TAB = (By.XPATH, '//a[text()="Профиль"]')
    HISTORY_ORDER_TAB = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    ORDER_CARDS = (By.CSS_SELECTOR, "[class*='OrderHistory_list'] > li")
    ORDER_CARD_ID = (By.CSS_SELECTOR, "[class*='OrderHistory_list'] .text_type_digits-default")

