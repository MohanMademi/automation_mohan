

import pyotp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from telnetlib import EC
import time



TOTP_KEY = "S2U6RKZR4T5PHRXLXOE5LTUXSFG2PS3T"
SUCCESS = 5
ERROR = -5



def generate_totp(secret):
    try:
        generate_totp = pyotp.TOTP(secret).now()
        return generate_totp
    except Exception as x:
        return [ERROR, x]




def login_totp():
    driver = webdriver.Chrome()
    driver.get("https://trade.fyers.in/")
    driver.maximize_window()



    driver.find_element(By.ID, "login_client_id").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@class='form-control text-uppercase mt-md-3 validate client_id']").send_keys("XM31487")
    time.sleep(2)
    driver.find_element(By.ID, "clientIdSubmit").click()
    time.sleep(3)



    generate_totp_result = generate_totp(secret=TOTP_KEY)
    print(generate_totp_result)
    driver.find_element(By.XPATH, "//Input[@id='first']").send_keys(generate_totp_result)
    time.sleep(2)
    driver.find_element(By.ID, "confirmOtpSubmit").click()
    time.sleep(5)


    driver.find_element(By.CSS_SELECTOR, "#pin-container>#first").send_keys("9642")
    time.sleep(2)
    driver.find_element(By.ID, "verifyPinSubmit").click()
    time.sleep(15)


    # iframe
    wait=WebDriverWait(driver,10)
    time.sleep(3)
    wait.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.XPATH, "//iframe[@frameborder='0' or @allowtransparency='true']")))
    print("iframe sucessfull")
    time.sleep(8)

    # driver.switch_to.frame("riskDisclosurePopup")
    # driver.find_element(By.XPATH,"//button[@id='confirmRiskDisclosure']").click()
    # print("frame completed")


     # watchlist
    driver.find_element(By.XPATH, "//div[@class='headerButton-mQBvegEO button-xNqEcuN2 button-GwQQdU8S apply-common-tooltip isInteractive-GwQQdU8S']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@class='search-ZXzPWcCf upperCase-ZXzPWcCf input-qm7Rg5MB']").send_keys("ZOMATO")
    time.sleep(2)

    driver.find_element(By.XPATH, "//span[@class='button-w6lVe_oI action-oRSs8UQo addAction-oRSs8UQo apply-common-tooltip']").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"//span[@class='button-w6lVe_oI action-oRSs8UQo targetAction-oRSs8UQo apply-common-tooltip']").click()
    time.sleep(10)

    print("watchlist showing completed")
    driver.close()


login_totp()
