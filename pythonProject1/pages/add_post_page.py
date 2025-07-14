import time
from pages.base_page import BasePage
from resources.locators import AddPostLocators


class AddPostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_add_post_header(self):
        return self.is_displayed(AddPostLocators.ADD_POST_HEADER)

    # --- Offer Form Methods ---
    def select_offers_category(self):
        self.click(AddPostLocators.OFFERS_RADIO)

    def enter_mobile(self, number):
        self.send_keys(AddPostLocators.MOBILE_INPUT, number)

    def enter_name(self, name):
        self.send_keys(AddPostLocators.NAME_INPUT, name)

    def enter_work_position(self, position):
        self.send_keys(AddPostLocators.WORK_POSITION_INPUT, position)

    def enter_email(self, email):
        self.send_keys(AddPostLocators.EMAIL_INPUT, email)

    def click_save(self):
        self.click(AddPostLocators.SAVE_BUTTON)

    def click_clear(self):
        self.click(AddPostLocators.CLEAR_BUTTON)

    # --- DS Collection Form ---
    def select_ds_collection_category(self):
        self.click(AddPostLocators.DS_COLLECTION_RADIO)

    # --- advertisement Form ---
    def select_advertisement_category(self):
        self.click(AddPostLocators.ADVERTISEMENT_RADIO)

