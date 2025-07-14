import unittest
from selenium import webdriver
from pages.login_page import LoginPage  # Import the LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your WebDriver
        self.driver.get("http://127.0.0.1:4723")  # Replace with the login URL

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("admin@gmail.com")
        login_page.enter_password("12345678")
        login_page.click_login()

        # Add an assertion to validate the login
        self.assertIn("Dashboard", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
