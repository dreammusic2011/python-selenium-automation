from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):

    SIGN_IN_TXT = (By.CSS_SELECTOR, "[class*= 'styles_ndsHeading__HcGpD']")


    def verify_sign_in_text(self, expected_text):
        actual_text = self.find_element(*self.SIGN_IN_TXT).text
        assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login')
        sleep(6)
