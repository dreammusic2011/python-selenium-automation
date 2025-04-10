from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):

    SIGN_IN_TXT = (By.CSS_SELECTOR, "[class*= 'styles_ndsHeading__HcGpD']")
    T_AND_C = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")
    SIGN_IN_TEXT = (By.ID, 'username')
    CLICK_LOGIN = (By.ID, 'login')

    def verify_sign_in_text(self, expected_text):
        actual_text = self.find_element(*self.SIGN_IN_TXT).text
        assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"

    def open_terms_page(self):
        self.click(*self.T_AND_C)

    def type_email(self):
        self.input_text('noreply@noreply.com', *self.SIGN_IN_TEXT)
        self.wait_until_clickable_click(*self.CLICK_LOGIN)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions')