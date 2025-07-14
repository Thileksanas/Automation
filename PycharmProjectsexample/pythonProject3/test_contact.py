import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup method to initialize driver and WebDriverWait
#@pytest.fixture(scope='module')
def setup():
    desired_cap = {
        "appium:automationName": "UiAutomator2",
        "platformName": "Android",
        "appium:deviceName": "Testing_device",
        "appium:appPackage": "com.thivja.myapp",
        "appium:appActivity": "com.thivja.myapp.MainActivity"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    yield driver
    driver.quit()


def test_example1():
    name = "Sana"
    assert  name == "", "Your name"

    def test_example2():
        email = "sana@gmail.com"
        assert email == "", "Your email address"

    def test_example3():
        writehere = "hello sana"
        assert writehere == "", "Your text here"

def test_example():
    name="Sana"
    email="sana@gmail.com"
    writehere="hello sana"







