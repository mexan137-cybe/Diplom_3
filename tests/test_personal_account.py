import allure
from data.config import Url
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalAccount:

    @allure.title('Переход в личный кабинет')
    def test_redirect_to_personal_account(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        was_redirected = WebDriverWait(login_user, 10).until(EC.url_contains(Url.PROFILE_URL))
        assert was_redirected

    @allure.title('Переход в сторию заказов')
    def test_redirect_to_history_order(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_history_order()
        was_redirected = WebDriverWait(login_user, 10).until(EC.url_contains(Url.HISTORY_ORDER_URL))
        assert was_redirected

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_logout()
        was_redirected = WebDriverWait(login_user, 10).until(EC.url_contains(Url.LOGIN_URL))
        assert was_redirected

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_logout()
        was_redirected = WebDriverWait(login_user, 10).until(EC.url_contains(Url.LOGIN_URL))
        assert was_redirected
    