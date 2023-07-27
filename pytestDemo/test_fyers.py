# import pytest
import pyotp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telnetlib import EC
import time




TOTP_KEY = ""
SUCCESS = 5
ERROR = -5
expected_url = "https://trade.fyers.in/"
def generte_totp(secret):
    try:
        generate_totp = pyotp.TOTP(secret).now()
        return generate_totp

    except Exception as x:
        return[ERROR,x]





# @pytest.fixture(scope="class")
def login_totp():
    driver = webdriver.Chrome()
    driver.get("https://trade.fyers.in/")
    driver.maximize_window()
    # yield driver
    # driver.quit()

    driver.find_element(By.ID,"fy_client_id").send_keys("XM31487")
    time.sleep(2)
    driver.find_element(By.ID,"clientIdSubmit").click()
    time.sleep(3)

    generate_totp_result = generate_totp(secret=TOTP_KEY)
    print("generate_totp_result")

    driver.find_element(By.XPATH,"//Input[@id='first']").send_keys(generate_totp_result)
    time.sleep(2)
    driver.find_element(By.ID, "confirmOtpSubmit").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#pin-container>#first").send_keys("9642")
    time.sleep(2)
    driver.find_element(By.ID,"verifyPinSubmit").click()
    time.sleep(3)


    #iframe

    wait = WebDriverWait(driver,10)
    time.sleep(2)
    wait.until()(EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.XPATH,"//iframe['@frameborder=0 or @allowtransparency=true']")))
    print("login completed")



    driver.switch_to.alert().accept()
    time.sleep(4)
    print("jhfksl")

    #watchlist
    driver.find_element(By.XPATH,"//div[@class='buttonWrap-uV8zMgPt']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//[@class='search-Hsmn_OWX upperCase-Hsmn_OWX input-3n5_2-hI']").send_keys("ZOMATO")
    time.sleep(2)
    driver.find_element(By.XPATH,"//[@class='close-2sLSJydP']").click()
    time.sleep(2)
    print("watchlist showing completed")
