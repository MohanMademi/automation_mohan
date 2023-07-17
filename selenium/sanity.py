from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the application homepage
driver.get("http://www.google.com")

# Perform sanity test steps
# Example 1: Verify the logo is displayed
logo_element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/img")
assert logo_element.is_displayed()
if logo_element.is_displayed():
    print("success")
else:
    print("failed")

# Example 2: Verify search functionality
# search_input = driver.find_element(By.ID,"search-input")
# search_button = driver.find_element(By.ID,"search-button")
#
# # Enter a search query
# search_input.send_keys("example query")
#
# # Click the search button
# search_button.click()
#
# # Example 3: Verify navigation functionality
# nav_link = driver.find_element(By.LINK_TEXT,"About Us")
# nav_link.click()
#
# # Verify the page title after navigation
# assert "About Us" in driver.title

# Close the browser
driver.quit()



# Verify that the application logo is displayed on the homepage.
# Test the search functionality by entering a search query and clicking the search button.
# Check the navigation functionality by clicking a navigation link and verifying the resulting page's title.