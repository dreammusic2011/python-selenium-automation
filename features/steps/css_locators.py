from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep

# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome()
# driver.maximize_window()


# open the url
# driver.get('https://www.amazon.com/')
# sleep(10)
# #find element
# driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1").click()
# sleep(2)
#
# # click sign in
# driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
# sleep(5)
#
# # find element
# driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
# driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']")
# driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
# driver.find_element(By.CSS_SELECTOR, "#ap_email")
# driver.find_element(By.CSS_SELECTOR, "#ap_password")
# driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
# driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")
# driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
# driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")


# @given('Open target.com')
# def step_open_target(context):
#     driver.get("https://www.target.com/")
#
# @when('Click on Cart icon')
# def click_the_cart(context):
#     driver.find_element(By.CSS_SELECTOR, "[href*='/cart?prehydrateClick=true']").click()
#     sleep(2)
#
# @then('Verify Cart is empty')
# def verify_cart_is_empty(context):
#     actual_text = driver.find_element(By.CSS_SELECTOR, "[data-test*='boxEmptyMsg']").text
#
#     expected_text = 'Your cart is empty'
#     assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"
#
#     print("Test passed.")
#
#
#
# @given('Open target.com')
# def step_open_target(context):
#     driver.get("https://www.target.com/")
#
# @when('Click Sign In')
# def sign_in(context):
#     driver.find_element(By.ID, 'account-sign-in').click()
#     sleep(2)
#
# @when('Sign In from menu')
# def menu_sign_in(context):
#     driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
#     sleep(2)
#
# @then('Verify sign in page')
# def verify_sign_in_form(context):
#     actual_text = driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading__HcGpD']").text
#
#     expected_text = 'Sign into your Target account'
#     assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"
#
#     print("Test passed.")