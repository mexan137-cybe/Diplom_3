import allure
from data.config import Url
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def open(self) -> 'ForgotPasswordPage':
        self.open_url(Url.BASE_URL + Url.FORGOT_PASSWORD_URL)
        return self

    @allure.step("Заполнить поле «Email»")
    def fill_email(self, value: str) -> None:
        self.type(ForgotPasswordLocators.EMAIL_INPUT, value)

    @allure.step("Нажать на кнопку «Восстановить»")
    def click_recovery_button(self) -> None:
        self.js_click(ForgotPasswordLocators.RECOVERY_BUTTON)