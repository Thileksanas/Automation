import pytest
from appium import webdriver
from pages.contact_us_page import ContactUsPage

class TestContactUs:
    @pytest.fixture(scope="class")
    def setup(self, request):
        desired_cap = {
            "appium:automationName": "UiAutomator2",
            "platformName": "Android",
            "appium:deviceName": "Testing_device",
            "appium:appPackage": "com.thivja.myapp",
            "appium:appActivity": "com.thivja.myapp.MainActivity"
        }
        driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)
        request.cls.driver = driver
        yield
        driver.quit()

    @pytest.mark.usefixtures("setup")
    class TestContactUsForm:
        def test_valid_contact_form_submission(self):
            contact_page = ContactUsPage(self.driver)
            contact_page.fill_contact_form("Sana", "sana@gmail.com", "Hello Sana")
            contact_page.click_send()
            # Add assertion for success message or result if applicable

        def test_invalid_contact_form_empty_name(self):
            contact_page = ContactUsPage(self.driver)
            contact_page.fill_contact_form("", "sana@gmail.com", "Hello Sana")
            contact_page.click_send()
            # Add assertion for error message or result

        def test_invalid_contact_form_invalid_email(self):
            contact_page = ContactUsPage(self.driver)
            contact_page.fill_contact_form("San", "sanagmail", "Hello San")
            contact_page.click_send()
            # Add assertion for error message or result
