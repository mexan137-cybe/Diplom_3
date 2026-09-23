import allure
from data.config import Url
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

class TestPersonalAccount:

    @allure.title('Переход в личный кабинет')
    def test_redirect_to_personal_account(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        main_page.wait_url_contains(Url.PROFILE_URL)
        assert main_page.get_current_url() == (Url.BASE_URL + Url.PROFILE_URL)

    @allure.title('Переход в сторию заказов')
    def test_redirect_to_history_order(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_history_order()
        main_page.wait_url_contains(Url.HISTORY_ORDER_URL)
        assert main_page.get_current_url() == (Url.BASE_URL + Url.HISTORY_ORDER_URL)

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_logout()
        profile_page.wait_url_contains(Url.LOGIN_URL)
        assert main_page.get_current_url() == (Url.BASE_URL + Url.LOGIN_URL)
    