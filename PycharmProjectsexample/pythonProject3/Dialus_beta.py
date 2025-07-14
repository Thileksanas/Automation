import os
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a directory for screenshots
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

def take_screenshot(driver, name):
    file_path = os.path.join(screenshot_dir, f"{name}.png")
    driver.get_screenshot_as_file(file_path)
    print(f"Screenshot saved to {file_path}")

desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "Testing_device",
    "appium:appPackage": "com.dialus.lk.app",
    "appium:appActivity": "com.dialus.lk.app.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)

wait = WebDriverWait(driver, 60)

# Example: Take a screenshot after clicking "Show more"
Showmore_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Show more"]/android.widget.ImageView')))
Showmore_icon.click()
time.sleep(3)
take_screenshot(driver, "show_more_clicked")

Showmore_bank = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Banks, "]')))
Showmore_bank.click()
time.sleep(3)
take_screenshot(driver, "show_more_banks_clicked")

More_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '(//android.widget.TextView[@text=""])[1]')))
More_nsb.click()
time.sleep(3)

Share_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
Share_nsb.click()
time.sleep(3)
driver.back()

edit_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="Edit"]')))
edit_nsb.click()
time.sleep(3)

editok_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')))
editok_nsb.click()
time.sleep(3)

call_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.ImageView')))
call_nsb.click()
time.sleep(3)
driver.back()
driver.back()

whatsapp_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.widget.ImageView')))
whatsapp_nsb.click()
time.sleep(3)

whatsapp1_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.whatsapp:id/contactpicker_text_container"])[5]')))
whatsapp1_nsb.click()
time.sleep(3)

send_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Send"]')))
send_nsb.click()
time.sleep(3)

send1_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Send"]')))
send1_nsb.click()
take_screenshot(driver, "whatsapp_message_sent")
time.sleep(3)
driver.back()
driver.back()

tele_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.widget.ImageView')))
tele_nsb.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
teleok_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')))

teleok_nsb.click()
time.sleep(3)
driver.back()
driver.back()
driver.back()

driver.quit()
# You can repeat the `take_screenshot` method after each significant interaction.
# For instance, after opening, editing, or sharing.

# Example: After sending via WhatsApp
# send_nsb = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Send"]')))
# send_nsb.click()
# time.sleep(3)
# take_screenshot(driver, "whatsapp_message_sent")

# Remember to take screenshots for critical steps or where debugging is needed.


