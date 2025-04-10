from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResults(driver)
        self.sign_in_page = SignInPage(driver)
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)


# app = Application(driver)
# app.header.search()
# app.search_results_page.verify_search_results()