from pages.base_page import BasePage
from resources.locators import FreeListingLocators

class FreeListingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_free_listing_button(self):
        self.click(FreeListingLocators.FREE_LISTING_BUTTON)

    def select_district(self):
        self.click(FreeListingLocators.DISTRICT_DROPDOWN)
        self.click(FreeListingLocators.DISTRICT_OPTION)

    def select_city(self):
        self.click(FreeListingLocators.CITY_DROPDOWN)
        self.click(FreeListingLocators.CITY_OPTION)

    def enter_name(self, name):
        self.send_keys(FreeListingLocators.NAME_INPUT, name)

    def enter_address(self, address):
        self.send_keys(FreeListingLocators.ADDRESS_INPUT, address)

    def enter_base_category(self, category):
        self.send_keys(FreeListingLocators.BASE_CATEGORY_INPUT, category)

    def enter_description(self, description):
        self.send_keys(FreeListingLocators.DESCRIPTION_INPUT, description)

    def enter_phone(self, phone):
        self.send_keys(FreeListingLocators.PHONE_INPUT, phone)

    def click_save(self):
        self.click(FreeListingLocators.SAVE_BUTTON)
