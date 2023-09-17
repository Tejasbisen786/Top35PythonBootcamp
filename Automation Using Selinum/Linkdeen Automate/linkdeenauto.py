from selenium import webdriver
import time

# Path to the ChromeDriver executable
chromedriver_path = "path_to_chromedriver.exe"  # Replace with the actual path

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open LinkedIn
driver.get("https://www.linkedin.com")

# Assuming you've already logged in, you can manually log in or automate it if needed

# Navigate to the pending invitations page
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")

# Scroll down to load more pending invitations (adjust the number of scrolls as needed)
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find and accept the connection requests
accept_buttons = driver.find_elements_by_xpath("//button[text()='Accept']")
for button in accept_buttons:
    button.click()
    time.sleep(1)  # Add a small delay to avoid rapid clicks

# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
