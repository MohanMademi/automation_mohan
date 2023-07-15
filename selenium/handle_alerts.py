from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[2]").click()
time.sleep(4)
alert = Alert(driver)
alert_text = alert.text
alert.accept()
time.sleep(4)
# alert.dismiss()

