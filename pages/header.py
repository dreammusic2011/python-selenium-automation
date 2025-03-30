from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton'")

    def search(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

