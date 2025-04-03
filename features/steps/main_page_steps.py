from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# SEARCH_FIELD = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
# HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")

@given('Open target page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_FIELD),
        message='Search field not clickable'
    )


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results_page.verify_search_results(expected_text)