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