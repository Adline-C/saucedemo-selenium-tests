from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

time.sleep(2)
# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

time.sleep(2)

# Click login
driver.find_element(By.ID, "login-button").click()

time.sleep(7)

driver.quit()