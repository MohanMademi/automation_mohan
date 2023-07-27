from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
cookie= driver.get_cookies()
print(cookie)

# driver.delete_cookie("")
# driver.delete_all_cookies()
driver.quit()
