from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton'")
    SIGN_IN = (By.ID, "account-sign-in")
    SIGN_IN_NAV = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")




    def search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.wait_until_clickable_click(*self.SEARCH_BUTTON)
        sleep(9)

    def sign_in(self):
        self.click(*self.SIGN_IN)

    def sign_in_navigate(self):
        self.click(*self.SIGN_IN_NAV)
