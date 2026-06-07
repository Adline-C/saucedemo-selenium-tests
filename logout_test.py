from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)

driver.find_element(By.ID, "logout_sidebar_link").click()

time.sleep(2)

assert "saucedemo.com" in driver.current_url

print("Logout Test Passed")

driver.quit()