from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AppiumBy

from appium import webdriver

def get_driver():
    desired_cap = {
        "appium:automationName": "UiAutomator2",
        "platformName": "Android",
        "appium:deviceName": "addpost",
        "appium:appPackage": "com.thileepan.Add",
        "appium:appActivity": "com.thileepan.Add.MainActivity"
    }
    return webdriver.Remote('http://127.0.0.1:4723', desired_cap)

#offer
class OfferPage(BasePage):
    OFFER_HEADING = (MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')
    IMAGE_UPLOAD = (MobileBy.XPATH, '//android.widget.TextView[@text="Tap to upload your image"]')
    PERMISSION_ALLOW = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    FIRST_IMAGE = (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')
    CROP_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')
    DESCRIPTION = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')
    IMAGE_LINK = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')
    SAVE_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')
    CLEAR_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')

    def fill_offer(self, heading, description, image_link):
        self.send_keys(self.OFFER_HEADING, heading)
        self.click(self.IMAGE_UPLOAD)
        self.click(self.PERMISSION_ALLOW)
        self.click(self.FIRST_IMAGE)
        self.click(self.CROP_BUTTON)
        self.send_keys(self.DESCRIPTION, description)
        self.send_keys(self.IMAGE_LINK, image_link)
        self.click(self.SAVE_BUTTON)

    def clear_offer(self):
        self.click(self.CLEAR_BUTTON)


#ds

class DSCollectionPage(BasePage):
    HEADING = (MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')
    IMAGE_UPLOAD = (MobileBy.XPATH, '//android.widget.TextView[@text="Tap to upload your image"]')
    FIRST_IMAGE = (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')
    CROP_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')
    DESCRIPTION = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')
    IMAGE_LINK = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')
    SAVE_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')

    def fill_ds_collection(self, heading, description, image_link):
        self.send_keys(self.HEADING, heading)
        self.click(self.IMAGE_UPLOAD)
        self.click(self.FIRST_IMAGE)
        self.click(self.CROP_BUTTON)
        self.send_keys(self.DESCRIPTION, description)
        self.send_keys(self.IMAGE_LINK, image_link)
        self.click(self.SAVE_BUTTON)



#ads
class AdvertisementPage(BasePage):
    NAME = (MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')
    LOGO_UPLOAD = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Tap to upload your image"]')
    FIRST_IMAGE = (MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')
    CROP_BUTTON = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')
    IMAGE_LINK = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')
    SAVE_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')

    def fill_advertisement(self, name, image_link):
        self.send_keys(self.NAME, name)
        self.click(self.LOGO_UPLOAD)
        self.click(self.FIRST_IMAGE)
        self.click(self.CROP_BUTTON)
        self.send_keys(self.IMAGE_LINK, image_link)
        self.click(self.SAVE_BUTTON)
