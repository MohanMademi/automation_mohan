from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()
driver.get("https://seleniumhq.github.i0/seleniumldocs/api/java/index.html")

driver.switch_to.frame("package List Frame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)
