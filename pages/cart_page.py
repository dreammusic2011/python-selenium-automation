from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart(self, expected_text):
        self.wait_until_visible(*self.PRODUCT_TITLE)
        actual_text = self.find_element(*self.PRODUCT_TITLE).text
        assert expected_text.lower() in actual_text.lower(), f'Error. Text {expected_text} not in {actual_text}'