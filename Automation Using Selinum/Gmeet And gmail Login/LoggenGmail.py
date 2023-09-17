from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Path to the ChromeDriver executable
chromedriver_path = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with the actual path

#  Gmail login credentials
gmail_username = "bisentejas00@gmail.com"  # Replace with your Gmail username or email
gmail_password = "bisnetejs#123"  # Replace with your Gmail password


# Initialize the Chrome driver
driver=webdriver.Chrome()

# Open Gmail
driver.get("https://mail.google.com")

# Find the email input field and enter your username
email_field = driver.find_element(By.NAME, "identifier")
email_field.send_keys(gmail_username)
email_field.send_keys(Keys.RETURN)

# Wait for the password input field to appear and enter your password
time.sleep(3)  # Wait for the password field to appear
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(gmail_password)
password_field.send_keys(Keys.RETURN)

# Wait for the Gmail inbox to load (you can add more robust waiting here)
time.sleep(5)

# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()