from selenium import webdriver
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

# open the url
driver.get('https://www.amazon.com/')
sleep(10)

# find element
driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']").click()

sleep(5)

driver.find_element(By.XPATH, "//i[@role='presentation']")
driver.find_element(By.XPATH, "//input[@type='email']")
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.ID, "createAccountSubmit")


# open the url
driver.get('https://www.target.com/')

#Find element
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(1)

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(1)

driver.find_element(By.XPATH, "//span[text()='Sign in with password']").click()

driver.find_element(By.XPATH, "//span[text()='Sign in with password']")


# open the url
driver.get('https://www.target.com/')

# find element
driver.find_element(By.ID, "search").send_keys("bottle")

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(4)

# check test

actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

expected_text = 'bottle'
assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"

print("test case passed")