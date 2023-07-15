from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.facebook.com")
time.sleep(4)
driver.implicitly_wait(10)
driver.find_element(By.ID,"email").send_keys("6302935408")
time.sleep(5)