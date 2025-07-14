from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Desired Capabilities
desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Example_Device",
  "appium:appActivity": "com.kiristina.myapp.MainActivity",
  "appium:appPackage": "com.kiristina.myapp"
}

# Initialize Appium Driver
driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)

# Define Wait
wait = WebDriverWait(driver, 60)


# Function to Click and Assert Icon Navigation
def click_and_verify_icon(xpath, icon_name):
    try:
        # Wait for the icon to be clickable
        icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, xpath)))
        icon.click()
        time.sleep(3)  # Wait for the screen to load

        # Assert to check successful interaction (this can vary based on the app's response)
        # Example: Assert if the icon's click leads to a change in the app (mocked here with a placeholder assertion)
        assert driver.current_activity != desired_cap["appium:appActivity"], f"Navigation failed for {icon_name}"

        print(f"{icon_name} clicked successfully.")

        # Go back
        driver.back()
        time.sleep(3)

    except Exception as e:
        # Catch and report any issues
        assert False, f"Error while interacting with {icon_name}: {str(e)}"


# Test Cases for Each Icon
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Hospital"]/android.widget.ImageView', "Hospital")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Courier"]/android.widget.ImageView', "Courier")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Leasing"]/android.widget.ImageView', "Leasing")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Bank"]/android.widget.ImageView', "Bank")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="ATM"]/android.widget.ImageView', "ATM")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Super Market"]/android.widget.ImageView', "Supermarket")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Restaurant"]/android.widget.ImageView', "Restaurant")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="School"]/android.widget.ImageView', "School")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Hotel"]/android.widget.ImageView', "Hotel")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Cabs"]', "Cabs")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Gym"]/android.widget.ImageView', "Gym")
click_and_verify_icon('//android.view.ViewGroup[@content-desc="Show more"]/android.widget.ImageView', "Show more")

# Quit the Driver
driver.quit()
