from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
# time.sleep(2)
driver.execute_script("window.scrollTo(0,300);")
element =driver.find_element(By.ID,"country")
drp = Select(element)
# assert drp.first_selected_option.text == "canada"
# time.sleep(3)
drp.select_by_index(5)
time.sleep(3)
drp.select_by_value("canada")
time.sleep(2)
drp.select_by_visible_text("China")
time.sleep(3)
driver.close()