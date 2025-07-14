from pages.base_page import BasePage
from resources.locators import HomeLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_hospitals(self):
        self.click(HomeLocators.HOSPITALS)

    def click_courier(self):
        self.click(HomeLocators.COURIER)

    def click_leasing(self):
        self.click(HomeLocators.LEASING)

    def click_banks(self):
        self.click(HomeLocators.BANKS)

    def click_atm(self):
        self.click(HomeLocators.ATM)

    def click_supermarkets(self):
        self.click(HomeLocators.SUPERMARKETS)

    def click_restaurant(self):
        self.click(HomeLocators.RESTAURANT)

    def click_more(self):
        self.click(HomeLocators.MORE_BUTTON)

    def click_plus_button(self):
        self.click(HomeLocators.PLUS_BUTTON)

    def click_redio_button(self):
        self.click(HomeLocators.OFFERS_RADIO)

    def click_mobile_button(self):
        self.click(HomeLocators.MOBILE_NUMBER_INPUT)
