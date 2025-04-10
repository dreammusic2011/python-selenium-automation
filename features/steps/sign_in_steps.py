from behave import given, when, then



# @given('Open target page')
# def open_target_page(context):
#     context.app.main_page.open_main_page()

@when('Click sign in')
def sign_in(context):
    context.app.header.sign_in()

@when('Click sign in nav')
def sign_in_navigate(context):
    context.app.header.sign_in_navigate()

@then('Verify sign in opened for {expected_text}')
def verify_sign_in_text(context, expected_text):
    context.app.sign_in_page.verify_sign_in_text(expected_text)