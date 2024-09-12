from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open URL
driver.get('https://www.target.com/')

# Search field
driver.find_element(By.XPATH, "//*[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(3)

# Search button
driver.find_element(By.XPATH, "//*[contains(@class, 'hHZPQy')]").click()

sleep(1)

driver.find_element(By.ID, "login")

# Verification
actual_result = driver.find_element(By.XPATH, ("//button[span[text()='Sign in with password']]")).text
expected_result = 'Sign in with password'
assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'

print('test case passed')

sleep(10)

driver.quit()