from behave import given, when, then

@given('Open sign in page')
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in_page()