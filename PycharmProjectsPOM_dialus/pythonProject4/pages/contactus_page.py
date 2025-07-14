from appium.webdriver.common.mobileby import MobileBy
from utils.base_page import BasePage

class ContactUsPage(BasePage):
    # Locators
    NAME_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@text="Your name"]')
    EMAIL_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@text="Your email address"]')
    MESSAGE_FIELD = (MobileBy.XPATH, '//android.widget.EditText[@text="Your text here..."]')
    SEND_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Send"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Actions
    def fill_contact_form(self, name, email, message):
        self.send_keys(self.NAME_FIELD, name)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.MESSAGE_FIELD, message)

    def click_send(self):
        self.click(self.SEND_BUTTON)
