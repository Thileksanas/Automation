from pages.base_page import BasePage
from resources.locators import MoreLocators

class MorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_about_us(self):
        self.click(MoreLocators.ABOUT_US_BUTTON)

    def click_contact_us(self):
       self.click(MoreLocators.CONTACT_US_BUTTON)
