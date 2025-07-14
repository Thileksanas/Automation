from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired Capabilities
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "freelist",
    "appium:appPackage": "com.dialus.lk.app",
    "appium:appActivity": "com.dialus.lk.app.MainActivity"
}

# Initialize Appium Driver
driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)

# Define Wait
wait = WebDriverWait(driver, 60)

# Reporting Function
def execute_step(description, action):
    """
    Executes the given action and logs the result.

    :param description: Description of the step being performed
    :param action: Lambda function for the step
    """
    try:
        action()
        print(f"[PASS] {description}")
    except Exception as e:
        print(f"[FAIL] {description}. Error: {str(e)}")

# Start Test
print("Starting Free Listing Test...")

# Step: Select District
execute_step(
    "Click on 'Select District' dropdown",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select District"]/android.widget.ImageView')
    )).click()
)

execute_step(
    "Select 'Jaffna' from district options",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@text="Jaffna"]')
    )).click()
)

# Step: Select City
execute_step(
    "Click on 'Select City' dropdown",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select City"]/android.widget.ImageView')
    )).click()
)

execute_step(
    "Select 'Analaitivu' from city options",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@text="Analaitivu"]')
    )).click()
)

# Step: Enter Name
execute_step(
    "Enter 'Dialus' in the name textbox",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')
    )).send_keys("Dialus")
)

# Step: Enter Address
execute_step(
    "Enter 'Nallur, Jaffna' in the address textbox",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="Type your address"]')
    )).send_keys("Nallur, Jaffna")
)

# Step: Select Base Category
execute_step(
    "Click on base category search field",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')
    )).click()
)

execute_step(
    "Enter 'ATM' in the base category search",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')
    )).send_keys("ATM")
)

execute_step(
    "Select 'ATM' from the category results",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@text="ATM"]')
    )).click()
)

# Step: Enter Description
execute_step(
    "Enter 'Best quality' in the description textbox",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]')
    )).send_keys("Best quality")
)

# Step: Select Contact
execute_step(
    "Open contact dropdown",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.ImageView')
    )).click()
)

execute_step(
    "Select a mobile contact option",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.ScrollView[@content-desc="undefined flatlist"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
    )).click()
)

# Step: Enter Mobile Number
execute_step(
    "Enter mobile number '077886655'",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 71XXXXXXX"]')
    )).send_keys("077886655")
)

# Step: Save Entry
execute_step(
    "Click on 'Save' button",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')
    )).click()
)

# Step: Clear Fields
execute_step(
    "Click on 'Clear' button",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')
    )).click()
)

# Step: Fail Scenario - Attempt to Save without Required Fields
execute_step(
    "Attempt to save without entering all required fields",
    lambda: wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')
    )).click()
)

# End of Test
print("Free Listing Test Completed.")
driver.quit()
