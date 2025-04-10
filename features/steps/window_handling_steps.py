from behave import given, when, then
from time import sleep


# The target sign in link would not work.
# The full link also did not work
@given('Open sign in page')
def sign_in(context):
    context.app.main_page.open_main_page()
    context.app.header.sign_in()
    context.app.header.sign_in_navigate()
    #sleep(30)

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)

@when('Click on Target terms and conditions link')
def terms_and_conditions(context):
    context.app.sign_in_page.type_email()
    context.app.sign_in_page.open_terms_page()
    sleep(10)

@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.sign_in_page.verify_tc_opened()

@then('User can close new window and switch back to original')
def close_new_window(context):
    context.app.base_page.close()
    context.app.base_page.switch_to_window_by_id(context.original_window)

