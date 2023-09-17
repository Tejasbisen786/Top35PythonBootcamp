import os
from selenium import webdriver

# Set the path to your Sublime Text 3 executable
sublime_path = "C:\Program Files\Sublime Text 3\sublime_text.exe"  # Replace with the correct path on your system

# Specify the URL to open in the browser (you can use any URL)
url = "https://example.com"

# Configure Selenium to use a specific web driver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open the URL in the browser
    # driver.get(url)
    
    # Run the command to open Sublime Text using the specified path
    os.system(f'"{sublime_path}"')

    # You can add more automation code here if needed

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the Selenium WebDriver
    driver.quit()
