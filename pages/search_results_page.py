from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):


    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
    ADD_TO_CART_2 = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    SIDE_PNL_ATC = (By.CSS_SELECTOR, '[href="/cart"]')




    def verify_search_results(self, expected_text):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
        sleep(3)
        self.click(*self.ADD_TO_CART_2)


    def view_cart_checkout(self):
        sleep(3)
        self.wait_until_clickable_click(*self.SIDE_PNL_ATC)