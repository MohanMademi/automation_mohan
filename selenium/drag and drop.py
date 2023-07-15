from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
driver.execute_script("window.scrollTo(0,700);")
time.sleep(3)

drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID,"droppable")
actions= ActionChains(driver)

actions.drag_and_drop(drag,drop).perform()
time.sleep(4)

