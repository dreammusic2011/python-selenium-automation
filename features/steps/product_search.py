from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CIRCLE_LINKS = (By.CSS_SELECTOR, "[id*='altlmH4']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton'")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')


# Verify Links

@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify {link_amount} links')
def verify_links(context, link_amount):
    links = context.driver.find_elements(*CIRCLE_LINKS)
    assert len(links) == int(link_amount), f"Expected {link_amount} links, got {len(links)}"


# Search product and add to cart

@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com')


@when('search for {search_word}')
def verify_links(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)


@when('Add to cart')
def add_to_cart(context):
    sleep(7)
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='orderPickupButton']").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(2)
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-order-summary']").text


@then('Verify in cart for {expected_text}')
def verify_cart(context, expected_text):
    actual_text = context.driver.find_element(*PRODUCT_TITLE).text

    assert expected_text.lower() in actual_text.lower(), f'Error. Text {expected_text} not in {actual_text}'

# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)


# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)
#
#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     assert search_word.lower() in context.driver.current_url.lower(), \
#         f'Expected query not in {context.driver.current_url.lower()}'
