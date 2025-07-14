
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Testing_device",
  "appium:appPackage": "com.nivethika.helloworld",
  "appium:appActivity": "com.nivethika.helloworld.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)


wait = WebDriverWait(driver, 80)
url_button=driver.find_element(MobileBy.XPATH,'//android.widget.TextView[@text="https://www.dialus.lk/free_listing"]')
url_button.click()
time.sleep(5)
driver.back()