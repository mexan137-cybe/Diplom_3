import allure
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):

    def get_password_input(self):
        return self.find(ResetPasswordLocators.PASSWORD_INPUT)

    @allure.step("Заполнить поле «Пароль»")
    def fill_password(self, value: str) -> None:
        return self.type(ResetPasswordLocators.PASSWORD_INPUT, value)
    
    
    @allure.step("Нажать «Показать пароль»")
    def click_show_password(self) -> None:
        self.click(ResetPasswordLocators.PASSWORD_SHOW_HIDE_ICON)

    @allure.step("Проверить видимость пароля")
    def is_password_visible(self) -> bool:
        password_field = self.get_password_input()
        input_type = password_field.get_attribute("type")
        if input_type == "text":
            return True
        elif input_type == "password":
            return False
        else:
            raise ValueError(f"Неожиданный тип поля ввода: {input_type}")