from appium import webdriver
desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:appActivity": "com.example.android.contactmanager.ContactManager",
  "appium:appPackage": "com.example.android.contactmanager"
}

driver = webdriver.Remote(' http://127.0.0.1:4723',desired_cap)