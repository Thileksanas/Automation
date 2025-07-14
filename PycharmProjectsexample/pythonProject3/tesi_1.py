from appium import webdriver
import os
from appium.webdriver.common.mobileby import MobileBy
desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:appActivity": "com.example.android.contactmanager.ContactManager",
  "appium:appPackage": "com.example.android.contactmanager",
  "app": os.path.abspath("./ContactManager.apk")
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)

continue_button = driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/continue_button')
continue_button.click()



