import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):

    @allure.step("Нажать кнопку «Профиль» ")
    def click_to_profile(self)-> None:
        self.click(PersonalAccountLocators.PROFILE_TAB)

    @allure.step("Нажать кнопку «История заказов» ")
    def click_to_history_order(self)-> None:
        self.click(PersonalAccountLocators.HISTORY_ORDER_TAB)

    @allure.step("Нажать кнопку «Выход» ")
    def click_to_logout(self)-> None:
        self.js_click(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step("Кликнуть по единственному заказу в истории")
    def click_to_first_order(self) -> None:
        self.click(PersonalAccountLocators.ORDER_CARDS)

    @allure.step("Получить номер заказа из открытого модального окна деталей")
    def get_modal_order_id(self) -> str:
        element = self.wait_visible(PersonalAccountLocators.ORDER_CARD_ID)
        return element.text.strip()