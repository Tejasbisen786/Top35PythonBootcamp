from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.common.keys import Keys
import time



chromedriver_path = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with the actual path


# Google account login credentials
google_email = "bisentejas00@gmail.com"  # Replace with your Google email
google_password = "bisen_tejas#123"  # Replace with your Google password

# Google Meet link
meeting_link = "https://meet.google.com/bkv-gwzd-jur"  # Replace with your Google Meet link

# Initialize the Chrome driver
driver=webdriver.Chrome()


# Open Google Meet
driver.get("https://meet.google.com")

# Find and click the "Sign in" button
try:
    sign_in_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
    sign_in_button.click()
except:
    print("The 'Sign in' button was not found or is not accessible.")

# Find and enter the email address
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys(google_email)
email_field.send_keys(Keys.RETURN)

# Wait for the password field to appear and enter the password
time.sleep(3)  # Wait for the password field to appear
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(google_password)
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete (you can add more robust waiting here)
time.sleep(5)

# Open the Google Meet link
driver.get(meeting_link)

# Wait for the meeting page to load
time.sleep(5)

# Find and click the "Ask to join" button
try:
    join_button = driver.find_element(By.XPATH, "//span[text()='Ask to join']")
    join_button.click()
    print("Requesting entry to the meeting...")
except:
    print("Meeting might not be joinable or the 'Ask to join' button is not available.")

# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()