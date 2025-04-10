from time import sleep

from behave import given, when, then



@given('Open target page')
def open_target_main(context):
    context.app.main_page.open_main_page()

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)

@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results_page.verify_search_results(expected_text)



@when('Add to cart')
def add_to_cart(context):
    context.app.search_results_page.add_to_cart()
    sleep(5)

@when('Check out page')
def check_out_page(context):
    context.app.search_results_page.view_cart_checkout()

@then('Verify in cart for {expected_text}')
def verify_cart(context, expected_text):
    context.app.cart_page.verify_cart(expected_text)

