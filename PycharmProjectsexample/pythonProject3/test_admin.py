import unittest
import time
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Desired Capabilities
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "Testing_device",
    "appium:appPackage": "com.dialus.lk.app",
    "appium:appActivity": "com.dialus.lk.app.MainActivity"
}

# Driver setup
driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)
report = {}  # To store pass/fail status

def run_step(step_name, action):
    """
    Execute a test step and log the result in the report.
    :param step_name: Name of the test step
    :param action: Lambda or callable with the step actions
    """
    try:
        action()
        report[step_name] = "PASS"
        print(f"{step_name}: PASS")
    except Exception as e:
        report[step_name] = f"FAIL ({e})"
        print(f"{step_name}: FAIL ({e})")

wait = WebDriverWait(driver, 60)

wait = WebDriverWait(driver, 60)

# Footer 'More' button
run_step("Click on Footer More Button", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.TextView[@text=""]'))).click())
time.sleep(3)

# Free Listing button
run_step("Click on Free Listing Button", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Free listing, "]'))).click())
time.sleep(3)

# Select District
run_step("Open District Dropdown", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select District"]/android.widget.ImageView'))).click())
time.sleep(3)

run_step("Select District (Jaffna)", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Jaffna"]'))).click())
time.sleep(3)

# Select City
run_step("Open City Dropdown", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select City"]/android.widget.ImageView'))).click())
time.sleep(3)

run_step("Select City (Analaitivu)", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Analaitivu"]'))).click())
time.sleep(3)

# Input Name
run_step("Enter Name", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]'))).send_keys('Dial Bank of Jaffna'))
time.sleep(3)

# Input Address
run_step("Enter Address", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type your address"]'))).send_keys('Nallur, Jaffna, 4002'))
time.sleep(3)

# Select Category
run_step("Open Category Dropdown", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]'))).click())
time.sleep(3)

run_step("Search and Select Category", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]'))).send_keys('Bank'))
time.sleep(3)

run_step("Select Bank Category", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Banks, "]'))).click())
time.sleep(3)

# Input Description
run_step("Enter Description", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]'))).send_keys('Best bank of Jaffna'))
time.sleep(3)

# Input Mobile Number
run_step("Enter Mobile Number", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 71XXXXXXX"]'))).send_keys('776545678'))
time.sleep(3)

run_step("Add Additional Contact", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="+"]'))).click())
time.sleep(3)

# Add Landline Number
run_step("Open Contact Type Dropdown", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.ImageView[2]'))).click())
time.sleep(3)

run_step("Select Landline Option", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.ScrollView[@content-desc="undefined flatlist"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'))).click())
time.sleep(3)

run_step("Enter Landline Number", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 021XXXXXXX"]'))).send_keys('0216545678'))
time.sleep(3)

# Save Free Listing
run_step("Save Free Listing", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]'))).click())
time.sleep(3)

# Navigate Back
run_step("Navigate Back to Main Menu", lambda: driver.back())

wait = WebDriverWait(driver, 60)

# #addpost button
run_step("Click Add Post Button", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.TextView[@text="+"]'))).click())
time.sleep(3)

# #offers
run_step("Enter Offer Heading", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]'))).send_keys('KFC'))
time.sleep(2)

run_step("Click Offer Image Upload", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]'))).click())
time.sleep(2)

run_step("Allow Permission for Images", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'))).click())
time.sleep(2)

run_step("Select First Image", lambda: wait.until(EC.visibility_of_element_located(
    (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'))).click())
time.sleep(2)

run_step("Crop Selected Image", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]'))).click())
time.sleep(2)

run_step("Enter Offer Description", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]'))).send_keys('So spicy'))
time.sleep(2)

run_step("Enter Offer Image Link", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]'))).send_keys('www.kfc.com'))
time.sleep(2)

run_step("Save Free Listing", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]'))).click())
time.sleep(2)

wait = WebDriverWait(driver, 60)

# DS Collection steps using test_step
run_step("Select DS Collection Radio Button", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.TextView[@text="DS Collection"]'))).click())
time.sleep(3)

run_step("Enter DS Collection Heading", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]'))).send_keys('kfc'))
time.sleep(3)

run_step("Click DS Collection Image Upload", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]'))).click())
time.sleep(3)

run_step("Select First Image for DS Collection", lambda: wait.until(EC.visibility_of_element_located(
    (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'))).click())
time.sleep(3)

run_step("Crop Selected Image for DS Collection", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]'))).click())
time.sleep(3)

run_step("Enter DS Collection Description", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]'))).send_keys('No one brand spicy chicken'))
time.sleep(3)

run_step("Enter DS Collection Image Link", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]'))).send_keys('www.kfcc.com'))
time.sleep(3)

run_step("Save DS Collection Listing", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]'))).click())
time.sleep(3)

run_step("Navigate Back to Previous Screen", lambda: driver.back())

wait = WebDriverWait(driver, 60)

# Navigating to login and handling approvals
run_step("Click on Footer More Button", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.TextView[@text=""]'))).click())
time.sleep(3)

run_step("Click on Login Button", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login, "]'))).click())
time.sleep(3)

run_step("Enter Email Address", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Enter your email"]'))).send_keys('admin@gmail.com'))
time.sleep(3)

run_step("Enter Password", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.EditText[@text="Enter your password"]'))).send_keys('12345678'))
time.sleep(3)

run_step("Click on Login", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login"]'))).click())
time.sleep(3)

run_step("Handle Login Popup", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'))).click())
time.sleep(3)

# Business Approval
run_step("Navigate to Business Approval", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Business approval, request, 1"]'))).click())
time.sleep(3)

run_step("View Business Approval Request", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '(//android.widget.TextView[@text="View  "])[1]'))).click())
time.sleep(3)

run_step("Accept Business Approval", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]'))).click())
time.sleep(3)

run_step("Confirm Business Approval Acceptance", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]'))).click())
time.sleep(3)

run_step("Navigate Back to Main Menu", lambda: driver.back())
time.sleep(3)

# Offer Approval
run_step("Navigate to Offer Approval", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Offer approval, request, 1"]'))).click())
time.sleep(3)

run_step("Accept Offer Approval", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]'))).click())
time.sleep(3)

run_step("Confirm Offer Approval Acceptance", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]'))).click())
time.sleep(3)

run_step("Navigate Back to Main Menu", lambda: driver.back())
time.sleep(3)

# DS Collection Approval and Deletion
run_step("Navigate to DS Collection Approval", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="DS Collection approval, request, 1"]'))).click())
time.sleep(3)

run_step("Delete DS Collection Request", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'))).click())
time.sleep(3)

run_step("Confirm DS Collection Deletion", lambda: wait.until(EC.element_to_be_clickable(
    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]'))).click())
time.sleep(3)

run_step("Navigate Back to Main Menu", lambda: driver.back())
time.sleep(3)

run_step("Navigate Back to Main Menu Again", lambda: driver.back())
time.sleep(3)

run_step("Navigate to Home", lambda: wait.until(EC.presence_of_element_located(
    (MobileBy.XPATH, '//android.widget.TextView[@text=""]'))).click())


# Clean up
driver.quit()

# Print final report
print("\nFinal Report:")
for step, status in report.items():
    print(f"{step}: {status}")
