import sys
import os
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import DriverSetup
from pages.home_page import HomePage
from pages.free_listing_page import FreeListingPage
from resources.locators import HomeLocators, FreeListingLocators

class TestFreeListing:

    @classmethod
    def setup_class(cls):
        cls.driver = DriverSetup().get_driver()
        cls.wait = WebDriverWait(cls.driver, 100)
        cls.home_page = HomePage(cls.driver)
        cls.free_listing_page = FreeListingPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_free_listing_form(self):
        # Go to Add Post page
        self.wait.until(EC.presence_of_element_located(HomeLocators.PLUS_BUTTON))
        self.home_page.click_plus_button()
        time.sleep(2)

        # Click Free Listing and fill form
        self.wait.until(EC.presence_of_element_located(FreeListingLocators.FREE_LISTING_BUTTON))
        self.free_listing_page.click_free_listing_button()
        time.sleep(1)

        self.free_listing_page.select_district()
        self.free_listing_page.select_city()
        self.free_listing_page.enter_name("Thileksana Jeya")
        self.free_listing_page.enter_address("123, Test Road, Colombo")
        self.free_listing_page.enter_base_category("Business")
        self.free_listing_page.enter_description("Automated Free Listing form fill.")
        self.free_listing_page.enter_phone("0771112233")
        self.free_listing_page.click_save()

        print("✅ Free Listing form is filled and submitted successfully.")
        time.sleep(2)
