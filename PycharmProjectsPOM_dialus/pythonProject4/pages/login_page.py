from selenium.webdriver.common.by import By
from base_page import BasePage  # Assuming  base_page.py file in pages/

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "admin@gmail.com")
    PASSWORD_FIELD = (By.ID, "12345678")
    LOGIN_BUTTON = (By.ID, "loginButton")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Page Actions
    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
