from appium import webdriver
import pytest
import time

from appium.webdriver.common.mobileby import MobileBy



desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Testing_device",
  "appium:appPackage": "com.nivethika.helloworld",
  "appium:appActivity": "com.nivethika.helloworld.MainActivity"
}


driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)

def test_navigate():

    print('url_button')
url_button=driver.find_element(MobileBy.XPATH,'//android.widget.TextView[@text="https://www.dialus.lk/free_listing"]')
url_button.click()