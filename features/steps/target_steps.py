from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('the target page')
def open_main(context):
    context.driver.get('https://www.target.com')

@when('Click the cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, value="[href*='/cart?']").click()


@then('Verify search results')
def verify_search(context):
    actual_result = context.driver.find_element(By.XPATH, value="//*[contains(text(), 'Your cart is empty')]").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'



@given('the sign in page')
def open_main(context):
    context.driver.get('https://www.target.com')


@when('Click on sign in')
def click_signin(context):
    context.driver.find_element(By.XPATH, value="//*[text()='Sign in']").click()
    context.driver.find_element(By.CSS_SELECTOR, value=".sc-859e7637-0.hHZPQy").click()
    sleep(5)

@then('Verify sign in page')
def verify_signin(context):
    actual_result = context.driver.find_element(By.XPATH, value="//*[contains(text(), 'Sign in with password')]").text
    expected_result = 'Sign in with password'
    assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'