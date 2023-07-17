from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the application homepage
driver.get("http://www.example.com")

# Perform smoke test steps
# Example 1: Verify the page title
expected_title = "Example Website"
assert expected_title == driver.title

# Example 2: Verify important elements are present
login_button = driver.find_element(By.ID,"login-button")
search_input = driver.find_element(By.ID,"search-input")
assert login_button.is_displayed() and search_input.is_displayed()

# Example 3: Perform a simple navigation
about_link = driver.find_element(By.LINK_TEXT,"About")
about_link.click()

# Verify the page title after navigation
assert "About" in driver.title

# Close the browser
driver.quit()
