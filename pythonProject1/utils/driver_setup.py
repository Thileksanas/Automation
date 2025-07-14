from appium import webdriver

class DriverSetup:
    def get_driver(self):
        desired_caps = {
            "appium:automationName": "UiAutomator2",
            "platformName": "Android",
            "appium:deviceName": "freelist",
            "appium:appPackage": "com.dialus.lk.app",
            "appium:appActivity": "com.dialus.lk.app.MainActivity"
        }
        driver = webdriver.Remote("http://localhost:4723", desired_caps)
        driver.implicitly_wait(10)
        return driver
