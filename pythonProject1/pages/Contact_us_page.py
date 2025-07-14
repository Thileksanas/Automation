from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from resources.locators import ContactUsLocators

class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def verify_contact_us_text(self):
        return self.wait.until(EC.presence_of_element_located(ContactUsLocators.CONTACT_US_TEXT))
