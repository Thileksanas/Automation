from pages.base_page import BasePage
from resources.locators import AboutUsLocators

class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_about_us_text(self):
        return self.is_displayed(AboutUsLocators.ABOUT_US_TEXT)
