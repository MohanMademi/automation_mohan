from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverwait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
element=WebDriverwait(driver,10).until(EC.element_to_be_clickable(By.ID,"email").send_keys("6302935408"))