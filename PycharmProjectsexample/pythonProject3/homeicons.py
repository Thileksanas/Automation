from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Example_Device",
  "appium:appActivity": "com.kiristina.myapp.MainActivity",
  "appium:appPackage": "com.kiristina.myapp"
}
driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)

wait = WebDriverWait(driver, 60)
hospital_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Hospital"]/android.widget.ImageView')))
hospital_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)

Courier_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Courier"]/android.widget.ImageView')))
Courier_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)

Leasing_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Leasing"]/android.widget.ImageView')))
Leasing_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Banks_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Bank"]/android.widget.ImageView')))
Banks_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
ATM_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="ATM"]/android.widget.ImageView')))
ATM_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Supermarkets_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Super Market"]/android.widget.ImageView')))
Supermarkets_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Restaurant_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Restaurant"]/android.widget.ImageView')))
Restaurant_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
School_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="School"]/android.widget.ImageView')))
School_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Hotels_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Hotel"]/android.widget.ImageView')))
Hotels_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Caps_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Cabs"]/android.widget.ImageView')))
Caps_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Gym_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Gym"]/android.widget.ImageView')))
Gym_icon.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
Showmore_icon = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Show more"]/android.widget.ImageView')))
Showmore_icon.click()
time.sleep(3)
driver.back()