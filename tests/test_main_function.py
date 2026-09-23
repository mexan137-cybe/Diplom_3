import allure
import pytest
from data.config import Url
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_created_page import OrderCreatedModal
from data.api_helper import get_one_ingredients_of_each_type

class TestMainFunction:

    @allure.title('Переход в конструктор')
    def test_redirect_to_constructors(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_constructor()
        login_page.wait_url_contains(Url.BASE_URL)
        assert login_page.get_current_url().rstrip('/') == Url.BASE_URL

    @allure.title('Переход в ленту заказов')
    def test_redirect_to_orders(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_orders()
        login_page.wait_url_contains(Url.ORDERS)
        assert login_page.get_current_url() == (Url.BASE_URL + Url.ORDERS)

    @pytest.mark.parametrize("ingredient",get_one_ingredients_of_each_type())
    @allure.title('Открытие окна с деталями об ингридиенте')
    def test_open_random_ingredient(self, login_user, ingredient):
        main_page = MainPage(login_user)
        ingredient_name = ingredient["name"]
        main_page.click_to_ingredient_by_name(ingredient_name)
        actual_title = main_page.get_modal_ingredient_title()
        assert actual_title == ingredient_name

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_modal_ingredient(self, login_user):
        main_page = MainPage(login_user)
        elements = get_one_ingredients_of_each_type()
        elements_name = elements[1]["name"]
        main_page.click_to_ingredient_by_name(elements_name)
        is_hiden = main_page.close_modals()
        assert is_hiden
        

    @allure.title("Проверка добавления соуса в конструктор через Drag and Drop")
    def test_add_sauce_to_constructor(self, login_user):
        main_page = MainPage(login_user)
        elements = get_one_ingredients_of_each_type()
        sauce_name = elements[1]["name"]  
        main_page.drag_and_drop_ingredient(sauce_name)   
        assert main_page.get_ingredient_count(sauce_name) == 1

    @allure.title("Залогиненный пользователь может оформить заказ.")
    def test_order_created(self, login_user):
        main_page = MainPage(login_user)
        elements = get_one_ingredients_of_each_type()
        sauce_name = elements[1]["name"]  
        main_page.drag_and_drop_ingredient(sauce_name)
        main_page.click_to_create_order_button()   
        order = OrderCreatedModal(login_user)
        order_id = order.get_order_id()
        assert order_id.isdigit() and order_id != "0000"
