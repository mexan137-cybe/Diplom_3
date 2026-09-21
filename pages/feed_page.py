import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    @allure.step("Получить список номеров всех заказов из Ленты")
    def get_all_order_numbers_from_feed(self) -> list[str]:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(FeedLocators.ORDER_NUMBERS_IN_FEED))
        elements = self.driver.find_elements(*FeedLocators.ORDER_NUMBERS_IN_FEED)
        return [el.text.replace("#", "").strip() for el in elements]
    
    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_counter_all_time_value(self) -> int:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FeedLocators.COUNTER_ALL_TIME))
        return int(element.text.strip())

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_counter_today_value(self) -> int:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FeedLocators.COUNTER_TODAY))
        return int(element.text.strip())

    @allure.step("Получить список номеров заказов из раздела «В работе»")
    def get_orders_in_progress_numbers(self) -> list[str]:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(FeedLocators.ORDERS_IN_PROGRESS))
        elements = self.driver.find_elements(*FeedLocators.ORDERS_IN_PROGRESS)
        return [el.text.strip() for el in elements]