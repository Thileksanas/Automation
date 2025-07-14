import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import HtmlTestRunner  # For generating HTML reports
import time

class AppiumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up Appium driver before tests run."""
        desired_cap = {
            "appium:automationName": "UiAutomator2",
            "platformName": "Android",
            "appium:deviceName": "Testing_device",
            "appium:appPackage": "com.dialus.lk.app",
            "appium:appActivity": "com.dialus.lk.app.MainActivity"
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)
        cls.wait = WebDriverWait(cls.driver, 180)

    def test_add_post(self):
        """Test adding a new post."""
        addpost_icon = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="+"]')))
        addpost_icon.click()
        time.sleep(3)

        offerhead_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
        offerhead_button.send_keys('KFC')
        time.sleep(2)

        offerimage_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]')))
        offerimage_button.click()
        time.sleep(2)

        offerallow_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')))
        offerallow_button.click()
        time.sleep(2)

        offerselectimage_button = self.wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
        offerselectimage_button.click()
        time.sleep(2)

        offerphotocrop_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]')))
        offerphotocrop_button.click()
        time.sleep(2)

        offerdescrip_textbox = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
        offerdescrip_textbox.send_keys('So spicy')
        time.sleep(2)

        offerimagelink_textbox = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
        offerimagelink_textbox.send_keys('www.kfc.com')
        time.sleep(2)

        offersave_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
        offersave_button.click()
        time.sleep(2)


        def driver_back(cls):
            """Navigate back using driver."""
            cls.driver.back()
            time.sleep(2)
        #ds
        def test_ds_post(self):
            """Test adding a new post."""

        ds_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="DS Collection"]')))
        ds_button.click()
        time.sleep(2)

        dshead_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
        dshead_button.send_keys('kfc')
        time.sleep(2)

        dsimage_button = self.wait.until(EC.element_to_be_clickable(
            (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]')))
        dsimage_button.click()
        time.sleep(2)

        dsselectimage_button = self.wait.until(EC.visibility_of_element_located((MobileBy.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
        dsselectimage_button.click()
        time.sleep(2)

        dsphotocrop_button = self.wait.until(EC.element_to_be_clickable(
            (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]')))
        dsphotocrop_button.click()
        time.sleep(2)

        dsdescrip_textbox = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
        dsdescrip_textbox.send_keys('No one brand spicy chicken')
        time.sleep(2)

        dsimagelink_textbox = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
        dsimagelink_textbox.send_keys('www.kfcc.com')
        time.sleep(2)

        dssave_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
        dssave_button.click()
        time.sleep(2)
        self.driver_back()

    # def driver_back(cls):
    #     """Navigate back using driver."""
    #     cls.driver.back()
    #     time.sleep(2)

    def test_login(self):
        """Test login functionality."""
        # Navigate to the login screen
        footmore_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
        footmore_button.click()
        time.sleep(3)

        login_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login, "]')))
        login_button.click()
        time.sleep(3)

        # Enter login credentials
        email_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Enter your email"]')))
        email_button.send_keys('admin@gmail.com')
        time.sleep(3)

        pw_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Enter your password"]')))
        pw_button.send_keys('12345678')
        time.sleep(3)

        # Submit login
        inlogin_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login"]')))
        inlogin_button.click()
        time.sleep(3)

        # Handle post-login popup
        loginpopup_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')))
        loginpopup_button.click()
        time.sleep(3)

        # Navigate back to the home screen or main workflow
        # self.driver_back()

        def driver_back(cls):
            """Navigate back using driver."""
            cls.driver.back()
            time.sleep(2)

        def test_business_approval(self):
            """Test business and offer approval workflow."""
            # Business approval workflow
            busi_button = self.wait.until(EC.element_to_be_clickable(
                (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Business approval, request, 1"]')))
            busi_button.click()
            time.sleep(3)

            view_button = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, '(//android.widget.TextView[@text="View  "])[1]')))
            view_button.click()
            time.sleep(3)

            accept_button = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]')))
            accept_button.click()
            time.sleep(3)

            acceptyes_button = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
            acceptyes_button.click()
            time.sleep(3)
            self.driver_back()

            # Offer approval workflow
            offe_button = self.wait.until(EC.element_to_be_clickable(
                (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Offer approval, request, 1"]')))
            offe_button.click()
            time.sleep(3)

            accept_button = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]')))
            accept_button.click()
            time.sleep(3)

            acceptyes_button = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
            acceptyes_button.click()
            time.sleep(3)
            self.driver_back()

            def test_ds_collection_approval(self):
                """Test DS Collection approval workflow."""
                # Navigate to DS Collection approval
                ds_button = self.wait.until(EC.element_to_be_clickable(
                    (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="DS Collection approval, request, 1"]')))
                ds_button.click()
                time.sleep(3)

                # Delete the request
                delete_button = self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]')))
                delete_button.click()
                time.sleep(3)

                # Confirm deletion
                yes_button = self.wait.until(
                    EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
                yes_button.click()
                time.sleep(3)

                # Navigate back three times
                self.driver_back()
                self.driver_back()
                self.driver_back()

                # Navigate to the home screen
                home_button = self.wait.until(
                    EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
                home_button.click()
                time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        """Close Appium driver after all tests are complete."""
        cls.driver.quit()

# Main block to run tests
# if __name__ == "__main__":
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports", report_name="AppiumTestReport"),
#         verbosity=2
#     )
