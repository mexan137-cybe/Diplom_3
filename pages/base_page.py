from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))
      
    def find(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, timeout=10) -> list[WebElement]:
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def click(self, locator) -> None:
        self.wait_clickable(locator).click()

    def js_click(self, locator) -> None:
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text: str) -> None:
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator) -> bool:
        try:
            return self.wait_visible(locator).is_displayed()
        except Exception:
            return False

    def scroll_to(self, locator) -> WebElement:
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def open_url(self, url: str) -> None:
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def current_window_handle(self) -> str:
        return self.driver.current_window_handle

    @property
    def window_handles(self) -> list:
        return self.driver.window_handles

    def switch_to_window(self, handle: str) -> None:
        self.driver.switch_to.window(handle)

    def close_current_window(self) -> None:
        self.driver.close()

    def wait_for_new_window(self, previous_handles) -> str:
        self.wait.until(lambda d: len(d.window_handles) > len(previous_handles))
        return (set(self.window_handles) - set(previous_handles)).pop()

    def wait_url_contains(self, text: str) -> None:
        self.wait.until(EC.url_contains(text))

    def get_current_url(self) -> str:
        return self.driver.current_url  

    def wait_invisible(self, locator) -> bool:
            return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def wait_presence(self, locator, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))