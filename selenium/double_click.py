from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
driver.execute_script("window.scrollTo(0,300);")
time.sleep(3)
DC =driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
actions = ActionChains(driver)
actions.double_click(DC).perform()
time.sleep(3)
driver.close()
