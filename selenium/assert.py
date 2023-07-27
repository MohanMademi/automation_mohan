from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)
driver.execute_script("window.scrollTo(0,700);")
time.sleep(3)
title=driver.title
assert "Google" in title
print("suc]178 cess")