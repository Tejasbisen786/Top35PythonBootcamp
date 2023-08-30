from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Path to the ChromeDriver executable
chromedriver_path = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with the actual path

# Initialize the Chrome driver
driver=webdriver.Chrome()

# driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open Google Chrome
driver.get("https://www.google.com")


# Find the search input field and enter your name
search_field = driver.find_element("name", "q")  # "q" is the name attribute of Google's search input field
search_field.send_keys("kodyfier.com")

search_field.send_keys(Keys.RETURN)


driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to appear


# Click on the first search result to open it in a new tab
first_result = driver.find_element("css selector", "h3")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).click(first_result).key_up(Keys.CONTROL).perform()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])



# Keep the browser window open for a few seconds
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
