from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
option1 = driver.find_element(By.ID,"male").click()
option2 = driver.find_element(By.ID,"female").click()
time.sleep(3)
driver.quit()