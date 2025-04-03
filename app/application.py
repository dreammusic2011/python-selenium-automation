from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResults(driver)


# app = Application(driver)
# app.header.search()
# app.search_results_page.verify_search_results()