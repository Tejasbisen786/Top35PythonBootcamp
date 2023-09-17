from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver=webdriver.Chrome()

# Gmail login credentials
gmail_username = "bisentejas00@gmail.com"  # Replace with your Gmail username or email
gmail_password = ""  # Replace with your Gmail password

# Path to the ChromeDriver executable

# Open Gmail
driver.get("https://mail.google.com")

# Find the email input field and enter your username
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys(gmail_username)

# Click the "Next" button
next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()
time.sleep(2)  # Wait for the next page to load

# Find the password input field and enter your password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(gmail_password)

# Click the "Next" button to log in
next_button = driver.find_element(By.ID, "passwordNext")
next_button.click()

# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
