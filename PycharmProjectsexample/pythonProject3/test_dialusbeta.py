
import unittest
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# i = 0
# while (1<10):
#     img = pyautogui

class AppiumTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Desired capabilities
        cls.desired_cap = {
            "appium:automationName": "UiAutomator2",
            "platformName": "Android",
            "appium:deviceName": "Testing_device",
            "appium:appPackage": "com.dialus.lk.app",
            "appium:appActivity": "com.dialus.lk.app.MainActivity"
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', cls.desired_cap)
        cls.wait = WebDriverWait(cls.driver, 60)

    def click_element(self, xpath, description):
        """Reusable method to click an element and log the result"""
        try:
            element = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, xpath)))
            element.click()
            print(f"{description} - Success")
        except TimeoutException:
            print(f"{description} - Failed (TimeoutException)")
            self.fail(f"{description} failed due to timeout.")
        except NoSuchElementException:
            print(f"{description} - Failed (NoSuchElementException)")
            self.fail(f"{description} failed due to missing element.")

    def test_workflow(self):
        """Test the full workflow"""
        # Click "Show More" icon
        self.click_element('//android.view.ViewGroup[@content-desc="Show more"]/android.widget.ImageView', "Show More Icon")

        # Click "Banks" option
        self.click_element('//android.view.ViewGroup[@content-desc="Banks, "]', "Show More Banks")

        # Click on "NSB" More options
        self.click_element('(//android.widget.TextView[@text=""])[1]', "More NSB")

        # Click "Share NSB"
        self.click_element('//android.widget.TextView[@text=""]', "Share NSB")
        self.driver.back()

        # Click "Edit NSB"
        self.click_element('//android.widget.TextView[@text="Edit"]', "Edit NSB")
        self.click_element('//android.widget.Button[@resource-id="android:id/button1"]', "Edit OK")

        # Click "Call NSB"
        self.click_element('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.ImageView', "Call NSB")
        self.driver.back()
        self.driver.back()

        # Click "WhatsApp NSB"
        self.click_element('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.widget.ImageView', "WhatsApp NSB")
        self.click_element('(//android.widget.LinearLayout[@resource-id="com.whatsapp:id/contactpicker_text_container"])[5]', "Select WhatsApp Contact")
        self.click_element('//android.widget.ImageButton[@content-desc="Send"]', "Send WhatsApp Message")
        self.click_element('//android.widget.ImageButton[@content-desc="Send"]', "Send WhatsApp Message Again")
        self.driver.back()
        self.driver.back()

        # Click "Telegram NSB"
        self.click_element('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.widget.ImageView', "Telegram NSB")
        self.click_element('//android.widget.Button[@resource-id="android:id/button1"]', "Telegram OK")

        # Click "Review NSB"
        self.click_element('(//android.widget.TextView[@text=""])[1]', "Review NSB")
        self.driver.back()
        self.driver.back()
        self.driver.back()

    @classmethod
    def tearDownClass(cls):
        # Close the Appium driver
        cls.driver.quit()


if __name__ == "__main__":
    import pytest
    import sys
    sys.argv = ["pytest", "--html=contact_us_report.html", "--self-contained-html"]
    pytest.main()
