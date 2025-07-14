from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Desired Capabilities
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "Testing_device",
    "appium:appPackage": "com.thivja.myapp",
    "appium:appActivity": "com.thivja.myapp.MainActivity"
}

# Initialize Appium Driver
driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)
wait = WebDriverWait(driver, 60)

# Function to Fill and Submit the Contact Us Form
def fill_contact_form(name, email, message, test_case):
    try:
        # Fill "Your name" field
        name_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your name"]')))
        name_textbox.clear()
        name_textbox.send_keys(name)
        time.sleep(2)

        # Fill "Your email address" field
        email_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your email address"]')))
        email_textbox.clear()
        email_textbox.send_keys(email)
        time.sleep(2)

        # Fill "Your text here..." field
        writehere_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your text here..."]')))
        writehere_textbox.clear()
        writehere_textbox.send_keys(message)
        time.sleep(2)

        # Click "Send" button
        send_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Send"]')))
        send_button.click()
        time.sleep(3)

        print(f"Test Case '{test_case}' Passed: Form submitted successfully.")

    except Exception as e:
        print(f"Test Case '{test_case}' Failed: {str(e)}")

# Test Cases
print("Starting Contact Us Form Test Cases...")

# Test Case 1: Valid inputs
fill_contact_form("Sana", "sana@gmail.com", "Hello Sana", "Valid Inputs")

# Test Case 2: Missing name
fill_contact_form("", "sana@gmail.com", "Hello Sana", "Missing Name")

# Test Case 3: Invalid email format
fill_contact_form("Sana", "sanagmail", "Hello Sanaa", "Invalid Email Format")

# Quit the Driver
driver.quit()

print("Contact Us Form Test Cases Completed.")
