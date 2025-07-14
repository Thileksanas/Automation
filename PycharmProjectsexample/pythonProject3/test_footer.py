from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired Capabilities
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "footer",
    "appium:appPackage": "com.nivethika.myapp",
    "appium:appActivity": "com.nivethika.myapp.MainActivity"
}

# Initialize Appium Driver
driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)

# Define Wait
wait = WebDriverWait(driver, 60)


# Function to navigate and generate a report
def navigate_and_report(xpath, screen_name):
    try:
        # Wait for the element and click
        element = wait.until(EC.presence_of_element_located((MobileBy.XPATH, xpath)))
        element.click()
        time.sleep(3)  # Wait for the screen to load

        # Log success
        print(f"[PASS] Navigation to '{screen_name}' successful.")

    except Exception as e:
        # Log failure
        print(f"[FAIL] Navigation to '{screen_name}' failed. Error: {str(e)}")


# Test Steps
print("Starting Test Suite...")

# Navigate to 'Home'
navigate_and_report('//android.widget.TextView[@text="Home"]', "Home")

# Navigate to 'Events'
navigate_and_report('//android.widget.TextView[@text="Events"]', "Events")

# Click 'OK' in 'Events'
navigate_and_report('//android.view.ViewGroup[@content-desc="OK"]', "Events OK")

# Navigate to 'Movies'
navigate_and_report('//android.widget.TextView[@text="Movies"]', "Movies")

# Click 'OK' in 'Movies'
navigate_and_report('//android.view.ViewGroup[@content-desc="OK"]', "Movies OK")

# Navigate to 'More'
navigate_and_report('//android.widget.TextView[@text="More"]', "More")

# End of Test
print("Test Suite Completed.")

# Quit Driver
driver.quit()
