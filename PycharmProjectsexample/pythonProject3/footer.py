from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "footer",
  "appium:appPackage": "com.nivethika.myapp",
  "appium:appActivity": "com.nivethika.myapp.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)

# Navigate to 'Home'
wait = WebDriverWait(driver, 60)
home_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Home"]')))
home_button.click()
time.sleep(3)

# Navigate to 'Events'
wait = WebDriverWait(driver, 60)
events_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Events"]')))
events_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
eventsok_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="OK"]')))
eventsok_button.click()
time.sleep(3)

# Navigate to 'Movies'
wait = WebDriverWait(driver, 60)
movies_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Movies"]')))
movies_button.click()
time.sleep(2)

wait = WebDriverWait(driver, 60)
moviesok_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="OK"]')))
moviesok_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
more_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="More"]')))
more_button.click()
time.sleep(3)
driver.back()