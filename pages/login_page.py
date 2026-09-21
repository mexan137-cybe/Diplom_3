import allure
from data.config import Url
from locators.login_page_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        self.open_url(Url.BASE_URL + Url.LOGIN_URL)
        return self
    
    @allure.step("Нажать на кнопку «Восстановить пароль»")
    def click_recovery_button(self) -> None:
        self.js_click(LoginLocators.FORGOT_PASSWORD)

    @allure.step("Заполнить поле «Пароль»")
    def fill_password(self, value: str) -> None:
        self.type(LoginLocators.PASSWORD_INPUT, value)

    @allure.step("Заполнить поле «Email»")
    def fill_email(self, value: str) -> None:
        self.type(LoginLocators.EMAIL_INPUT, value)

    @allure.step("Нажать «Войти»")
    def authorized_user(self):
        self.js_click(LoginLocators.LOGIN_BUTTON)

    @allure.step("Нажать «Конструктор»")
    def go_to_constructor(self) -> None:
        self.js_click(LoginLocators.CONSTRUCTOR)

    @allure.step("Нажать «Лента заказов»")
    def go_to_orders(self) -> None:
        self.js_click(LoginLocators.ORDERS)

