from selenium.webdriver.common.by import By

class FeedLocators:

    ORDER_NUMBERS_IN_FEED = (By.CSS_SELECTOR, "[class*='OrderFeed_list'] .text_type_digits-default")
    COUNTER_ALL_TIME = (By.CSS_SELECTOR, "div[class*='OrderFeed_orderFeed'] p[class*='text_type_digits-large']")
    COUNTER_TODAY = (By.CSS_SELECTOR, "div[class*='OrderFeed_orderFeed'] div:nth-child(2) p[class*='text_type_digits-large']")
    ORDERS_IN_PROGRESS = (By.XPATH, "//*[contains(text(), 'В работе')]/following-sibling::ul/li | //*[contains(text(), 'В работе')]/../ul/li")