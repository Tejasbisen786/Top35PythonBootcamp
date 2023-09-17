from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to the ChromeDriver executable
chromedriver_path = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with the actual path


# Initialize the Chrome driver
driver=webdriver.Chrome()

# Open LinkedIn
driver.get("https://www.linkedin.com")


# Click on the "Sign in with Google" button (if available)
google_sign_in_button = driver.find_element_by_xpath("//button[contains(text(), 'Sign in with Google')]")
if google_sign_in_button:
    google_sign_in_button.click()
    time.sleep(2)  # Give some time to load the Google login page

    # Fill in your Google login credentials
    google_email_field = driver.find_element_by_id("identifierId")
    google_email_field.send_keys("bisentejas00@gmail.com")  # Replace with your Google email
    google_email_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Give some time to load the next page

    # Fill in your Google password
    google_password_field = driver.find_element_by_name("password")
    google_password_field.send_keys("bisen_tejas#123")  # Replace with your Google password
    google_password_field.send_keys(Keys.RETURN)

    # After this step, you may be redirected back to LinkedIn

# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()








