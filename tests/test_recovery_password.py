import allure
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data.generators import generate_user_registration_data
from data.config import Url

class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver).open()
        login_page.click_recovery_button()
        forgot_page = ForgotPasswordPage(driver)
        assert forgot_page.page_is_visible()

    @allure.title('При вводе почты и нажатия кнопки "Восстановить" открывается восстановление пароля')
    def test_redirect_password(self, driver):
        login_page = LoginPage(driver).open()
        login_page.click_recovery_button()
        forgot_page = ForgotPasswordPage(driver)
        email = generate_user_registration_data()['email']
        forgot_page.fill_email(email)
        forgot_page.click_recovery_button()
        forgot_page.wait_url_contains(Url.RESET_PASSWORD_URL)     
        assert forgot_page.get_current_url() == (Url.BASE_URL + Url.RESET_PASSWORD_URL)

    @allure.title('Нажатие на кнопку "Показать пароль" показывает пароль')
    def test_show_password(self, driver):
        forgot_page = ForgotPasswordPage(driver).open()
        email = generate_user_registration_data()['email']
        forgot_page.fill_email(email)
        forgot_page.click_recovery_button()
        forgot_page.wait_url_contains(Url.RESET_PASSWORD_URL)
        reset_page = ResetPasswordPage(driver)
        password = generate_user_registration_data()['password']
        reset_page.fill_password(password)
        reset_page.click_show_password()
        assert reset_page.is_password_visible()
