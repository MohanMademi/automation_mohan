from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)

driver.execute_script("window.open('https://www.google.com');")
time.sleep(2)
new_window = driver.window_handles[0]
driver.switch_to.window(new_window)
time.sleep(3)
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

