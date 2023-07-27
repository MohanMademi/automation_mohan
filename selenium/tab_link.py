from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("www.facebook.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()
time.sleep(3)
link_element=driver.find_element(By.XPATH,"//*[@id='wikipedia-search-result-link']/a").click()
time.sleep(4)
driver.close()