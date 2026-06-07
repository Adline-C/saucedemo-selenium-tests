from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

error = driver.find_element(By.CLASS_NAME, "error-message-container").text

assert "Username and password do not match" in error

print("Invalid Login Test Passed")

driver.quit()