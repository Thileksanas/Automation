# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click(self, locator):
#         self.driver.find_element(*locator).click()
#
#     def is_displayed(self, locator):
#         return self.driver.find_element(*locator).is_displayed()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return False


    def click(self, locator):
      self.driver.find_element(*locator).click()


    def send_keys(self, locator, value):
      self.driver.find_element(*locator).send_keys(value)


    def is_element_displayed(self, locator):
      return self.driver.find_element(*locator).is_displayed()