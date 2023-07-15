from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
import pyautogui



# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Perform initial login test steps
username_input = driver.find_element(By.ID,"email")
password_input = driver.find_element(By.ID,"pass")
login_button = driver.find_element(By.NAME,"login")

username_input.send_keys("6302935408")
password_input.send_keys("mohan9642")
login_button.click()
time.sleep(6)
pyautogui.sleep(2)
pyautogui.press('enter')
print("gdjdk")
# alert = driver.switch_to.alert
# alert.dismiss()
# time.sleep(5)
#
create_post_area = driver.find_element(By.XPATH,"(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'])[5]").click()
print("hdbklk")