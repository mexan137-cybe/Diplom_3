from selenium.webdriver.common.by import By

class MainLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[.//p[text()="Личный Кабинет"]]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    MODAL_INGREDIENT_TITLE = (By.CSS_SELECTOR, "div[class*='Modal_modal'] .text_type_main-medium")
    CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket']")
    ORDERS = (By.XPATH, '//a[.//p[text()="Лента Заказов"]]')

    @staticmethod
    def ingredient_by_name(name: str) -> tuple:
        return By.XPATH, f'//a[.//img[@alt="{name}"]]'
    
    @staticmethod
    def ingredient_count(ingredient_name: str):
        return (By.XPATH,f'//a[.//img[@alt="{ingredient_name}"]]//p[contains(@class, "counter_counter__num")]')

class IngredientDetailsModalLocators:

    TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME = (By.XPATH,'//h2[text()="Детали ингредиента"]/following-sibling::p[contains(@class, "text_type_main-medium")]')
    STATS_ITEMS = (By.XPATH,'//h2[text()="Детали ингредиента"]/parent::div//li[contains(@class, "Modal_modal__statsListItem")]')
    CLOSE_BUTTON = (By.XPATH,'//h2[text()="Детали ингредиента"]/ancestor::section//button[contains(@class, "Modal_modal__close")]')

   