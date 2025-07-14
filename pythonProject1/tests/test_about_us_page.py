import unittest
from utils.driver_setup import DriverSetup
from pages.home_page import HomePage
from pages.more_page import MorePage
from pages.about_us_page import AboutUsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time


class TestAboutUsPage(unittest.TestCase):

    def setUp(self):
        self.driver = DriverSetup().get_driver()
        self.home_page = HomePage(self.driver)
        self.more_page = MorePage(self.driver)
        self.about_us_page = AboutUsPage(self.driver)

    def test_about_us(self):
        self.home_page.click_more()
        time.sleep(5)

        self.more_page.click_about_us()
        time.sleep(6)
        self.assertTrue(self.about_us_page.verify_about_us_text())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
