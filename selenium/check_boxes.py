from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
driver.find_element(By.ID,"sunday").click()
driver.find_element(By.ID,"monday").click()
time.sleep(3)
driver.find_element(By.ID,"tuesday").click()
driver.find_element(By.ID,"friday").click()
time.sleep(3)
driver.close()