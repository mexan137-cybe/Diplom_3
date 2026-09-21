from locators.order_created_locators import OrderCreatedLocators
from pages.base_page import BasePage

class OrderCreatedModal(BasePage):

    def get_order_id(self) -> str:
        return self.find(OrderCreatedLocators.ORDER_NUMBER).text

    def close(self) -> None:
        self.click(OrderCreatedLocators.CLOSE_BUTTON)
