from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


CIRCLE_LINKS = (By.CSS_SELECTOR, "[id*='altlmH4']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton'")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
SIDE_PNL_ATC = (By.CSS_SELECTOR, "[data-test*='orderPickupButton']")



@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify {link_amount} links')
def verify_links(context, link_amount):
    links = context.driver.find_elements(*CIRCLE_LINKS)
    assert len(links) == int(link_amount), f"Expected {link_amount} links, got {len(links)}"




@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com')


# @when('search for {search_word}')
# def verify_links(context, search_word):
#     # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
#     # context.driver.find_element(*SEARCH_BUTTON).click()
#     context.app.header.search(search_word)



# @when('Add to cart')
# def add_to_cart(context):
#     sleep(9)
#     context.driver.find_element(*ADD_TO_CART).click()
#     context.driver.wait.until(EC.element_to_be_clickable(SIDE_PNL_ATC)).click()
#     context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()

# @then('Verify in cart for {expected_text}')
# def verify_cart(context, expected_text):
    # actual_text = context.driver.find_element(*PRODUCT_TITLE).text
    #
    # assert expected_text.lower() in actual_text.lower(), f'Error. Text {expected_text} not in {actual_text}'
    # context.app.cart_page.verify_cart(expected_text)