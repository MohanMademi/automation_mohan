from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.facebook.com")
time.sleep(4)
driver.execute_script("window.scrollTo(0,100);")
time.sleep(4)