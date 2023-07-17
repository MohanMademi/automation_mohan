import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser

    # Set up any necessary configurations or options

    yield driver

    # Teardown: Quit the WebDriver after the test is complete
    driver.quit()

def test_facebook_login(browser):
    # Open the Facebook login page
    browser.get("https://www.facebook.com")

    # Perform interactions with the page using Selenium APIs
    username_field = browser.find_element(By.ID,"email")
    password_field = browser.find_element(By.ID,"pass")
    submit_button = browser.find_element(By.NAME,"login")

    username_field.send_keys("6302935408")
    password_field.send_keys("mohan9642")
    submit_button.click()

    # Perform assertions to verify the expected behavior
    # assert browser.title == "Facebook"
    assert browser.current_url == "https://www.facebook.com/"
    assert "Welcome" in browser.page_source