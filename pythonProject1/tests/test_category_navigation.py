import sys
import os
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import DriverSetup
from pages.home_page import HomePage
from pages.more_page import MorePage
from pages.about_us_page import AboutUsPage
from pages.Contact_us_page import ContactUsPage
from pages.add_post_page import AddPostPage
from resources.locators import (
    HomeLocators,
    MoreLocators,
    AboutUsLocators,
    ContactUsLocators,
    AddPostLocators,
    FreeListingLocators
)


class TestCategoryNavigation:

    @classmethod
    def setup_class(cls):
        cls.driver = DriverSetup().get_driver()
        cls.wait = WebDriverWait(cls.driver, 100)
        cls.home_page = HomePage(cls.driver)
        cls.more_page = MorePage(cls.driver)
        cls.about_us_page = AboutUsPage(cls.driver)
        cls.contact_us_page = ContactUsPage(cls.driver)
        cls.add_post_page = AddPostPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # def test_click_hospitals(self):
        self.wait.until(EC.presence_of_element_located(HomeLocators.HOSPITALS))
        self.home_page.click_hospitals()
        time.sleep(2)
        self.driver.back()

    # def test_click_courier(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.COURIER))
    #     self.home_page.click_courier()
    #     time.sleep(2)
    #     self.driver.back()

    # def test_click_leasing(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.LEASING))
    #     self.home_page.click_leasing()
    #     time.sleep(2)
    #     self.driver.back()
    #
    # def test_click_banks(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.BANKS))
    #     self.home_page.click_banks()
    #     time.sleep(2)
    #     self.driver.back()

    # def test_click_atm(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.ATM))
    #     self.home_page.click_atm()
    #     time.sleep(2)
    #     self.driver.back()
    #
    # def test_click_supermarkets(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.SUPERMARKETS))
    #     self.home_page.click_supermarkets()
    #     time.sleep(2)
    #     self.driver.back()
    #
    # def test_click_restaurant(self):
    #     self.wait.until(EC.presence_of_element_located(HomeLocators.RESTAURANT))
    #     self.home_page.click_restaurant()
    #     time.sleep(2)
    #     self.driver.back()

    def test_about_and_contact_us_flow(self):
        # Click on More
        self.wait.until(EC.presence_of_element_located(HomeLocators.MORE_BUTTON))
        self.home_page.click_more()
        time.sleep(2)

        # Click on About Us
        self.wait.until(EC.presence_of_element_located(MoreLocators.ABOUT_US_BUTTON))
        self.more_page.click_about_us()
        time.sleep(2)
        self.driver.back()


        #  Wait again to make sure More page is visible
        self.wait.until(EC.presence_of_element_located(MoreLocators.CONTACT_US_BUTTON))

        # Click on Contact Us
        self.more_page.click_contact_us()
        time.sleep(2)
        self.driver.back()
        self.driver.back()

        # Click "+" to go to Add Post
        self.wait.until(EC.presence_of_element_located(HomeLocators.PLUS_BUTTON))
        self.home_page.click_plus_button()
        time.sleep(2)

        # Offer Form
        self.add_post_page.select_offers_category()
        self.add_post_page.enter_mobile("0771234567")
        self.add_post_page.enter_name("Thileksana QA")
        self.add_post_page.enter_work_position("QA Engineer")
        self.add_post_page.enter_email("qa@example.com")
        self.add_post_page.click_save()
        time.sleep(2)

        self.add_post_page.click_clear()
        time.sleep(1)

        # DS Collection Form
        self.add_post_page.select_ds_collection_category()
        self.add_post_page.enter_mobile("0777654321")
        self.add_post_page.enter_name("DS Tester")
        self.add_post_page.enter_work_position("DS Manager")
        self.add_post_page.enter_email("dsqa@example.com")
        self.add_post_page.click_save()
        time.sleep(2)

        # Advertisemnet Form
        self.add_post_page.select_advertisement_category()
        self.add_post_page.enter_mobile("0777654321")
        self.add_post_page.enter_name("DS Tester")
        self.add_post_page.enter_work_position("DS Manager")
        self.add_post_page.enter_email("dsqa@example.com")
        self.add_post_page.click_save()
        time.sleep(2)

        self.driver.back()


