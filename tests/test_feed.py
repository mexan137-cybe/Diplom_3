import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.personal_account_page import PersonalAccountPage
from data.api_helper import create_order_via_api

class TestFeed:

    @allure.title('При открытии заказа, открывается окно с деталями')
    def test_open_orders(self, login_user, create_user):
        token = create_user.get("accessToken")
        expected_order_number = create_order_via_api(user_token= token)
        main_page = MainPage(login_user)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(login_user)
        profile_page.click_to_history_order()
        profile_page.click_to_first_order()
        actual_order_id = profile_page.get_modal_order_id()
        assert int(actual_order_id.replace('#', '')) == int(expected_order_number)

    @allure.title("Заказы пользователя из Истории отображаются на странице «Лента заказов»")
    def test_user_order_appears_in_feed(self, login_user, create_user):
        token = create_user.get("accessToken")
        expected_order_number = create_order_via_api(user_token=token)
        main_page = MainPage(login_user)
        main_page.go_to_orders()
        feed_page = FeedPage(login_user)
        feed_numbers = feed_page.get_all_order_numbers_from_feed()
        expected_int = int(expected_order_number)
        feed_ints = [int(num) for num in feed_numbers if num.isdigit()]
        assert (expected_int in feed_ints)

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_counter_all_time_increases_after_order(self, login_user, create_user):
        main_page = MainPage(login_user)
        main_page.go_to_orders()
        feed_page = FeedPage(login_user)
        initial_counter_value = feed_page.get_counter_all_time_value()
        token = create_user.get("accessToken")
        create_order_via_api(user_token=token)
        login_user.refresh()
        new_counter_value = feed_page.get_counter_all_time_value()
        assert new_counter_value > initial_counter_value

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_counter_today_increases_after_order(self, login_user, create_user):
        main_page = MainPage(login_user)
        main_page.go_to_orders()
        feed_page = FeedPage(login_user)
        initial_today_value = feed_page.get_counter_today_value()
        token = create_user.get("accessToken")
        create_order_via_api(user_token=token)
        login_user.refresh()
        new_today_value = feed_page.get_counter_today_value()
        assert new_today_value > initial_today_value

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_board(self, login_user, create_user):
        token = create_user.get("accessToken")
        expected_order_number = create_order_via_api(user_token=token)
        main_page = MainPage(login_user)
        main_page.go_to_orders()
        feed_page = FeedPage(login_user)
        expected_int = int(expected_order_number)
        login_user.refresh()
        progress_numbers = feed_page.get_orders_in_progress_numbers()
        progress_ints = [int(num) for num in progress_numbers if num.isdigit()]
        assert expected_int in progress_ints