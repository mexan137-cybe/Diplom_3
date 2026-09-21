import allure
from data.config import Url
from locators.main_page_locators import MainLocators, IngredientDetailsModalLocators
from pages.base_page import BasePage
from pages.order_created_page import OrderCreatedModal

class MainPage(BasePage):

    @allure.step("Открыть страницу конструктора")
    def open(self) -> 'MainPage':
            self.open_url(Url.BASE_URL)
            return self

    @allure.step("Нажать кнопку «Личный кабинет» ")
    def click_to_personal_account_button(self): 
        self.js_click(MainLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть по ингредиенту с именем '{ingredient_name}'")
    def click_to_ingredient_by_name(self, ingredient_name: str) -> None:
        locator = MainLocators.ingredient_by_name(ingredient_name)
        self.wait_clickable(locator)
        self.scroll_to(locator)
        self.js_click(locator)
        

    @allure.step("Получить название ингредиента из открытого модального окна")
    def get_modal_ingredient_title(self) -> str:
        element = self.wait_visible(IngredientDetailsModalLocators.INGREDIENT_NAME)
        return element.text

    @allure.step("Закрыть модальное окно ингридинта")
    def close_modals(self) -> None:
        self.js_click(IngredientDetailsModalLocators.CLOSE_BUTTON) 
        is_hiden = self.wait_invisible(IngredientDetailsModalLocators.CLOSE_BUTTON)
        return is_hiden

    @allure.title("Получаем количество позиций ингридиента в конструкторе")
    def get_ingredient_count(self, ingredient_name: str) -> int:
        counter_text = self.find(MainLocators.ingredient_count(ingredient_name)).text
        return int(counter_text)

    @allure.step("Перетащить ингредиент '{ingredient_name}' в конструктор")
    def drag_and_drop_ingredient(self, ingredient_name: str) -> None:
        ingredient_locator = MainLocators.ingredient_by_name(ingredient_name)
        source_element = self.wait_visible(ingredient_locator)
        self.scroll_to(ingredient_locator)
        target_element = self.wait_visible(MainLocators.CONSTRUCTOR_BASKET)
        js_drag_and_drop = """
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function (key, value) { this.data[key] = value; },
                        getData: function (key) { return this.data[key]; }
                    };
                    return event;
                }
        
                function dispatchEvent(element, eventType, dragEvent) {
                    if (element.dispatchEvent) {
                        element.dispatchEvent(dragEvent);
                    } else if (element.fireEvent) {
                        element.fireEvent("on" + eventType, dragEvent);
                    }
                }
        
                var source = arguments[0];
                var target = arguments[1];
        
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(source, 'dragstart', dragStartEvent);
        
                var dragEnterEvent = createEvent('dragenter');
                dispatchEvent(target, 'dragenter', dragEnterEvent);
        
                var dropEvent = createEvent('drop', dragStartEvent.dataTransfer);
                dropEvent.dataTransfer = dragStartEvent.dataTransfer;
                dispatchEvent(target, 'drop', dropEvent);
        
                var dragEndEvent = createEvent('dragend', dragStartEvent.dataTransfer);
                dispatchEvent(source, 'dragend', dragEndEvent);
                """
        self.driver.execute_script(js_drag_and_drop, source_element, target_element)

    @allure.step("Нажать кнопку «Оформить заказ» ")
    def click_to_create_order_button(self): 
        self.js_click(MainLocators.ORDER_BUTTON)
        return OrderCreatedModal(self.driver)

    @allure.step("Нажать «Лента заказов»")
    def go_to_orders(self) -> None:
        self.js_click(MainLocators.ORDERS)
        