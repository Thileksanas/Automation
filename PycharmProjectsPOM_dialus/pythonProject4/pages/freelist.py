from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "freelist",
  "appium:appPackage": "com.dialus.lk.app",
  "appium:appActivity": "com.dialus.lk.app.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)


wait = WebDriverWait(driver, 60)
freedis_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select District"]/android.widget.ImageView')))
freedis_dropdown.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
freedisselect_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Jaffna"]')))
freedisselect_dropdown.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
freecity_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select City"]/android.widget.ImageView')))
freecity_dropdown.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
freecityselect_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Analaitivu"]')))
freecityselect_dropdown.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
freename_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')))
freename_textbox.send_keys('Dialus')
time.sleep(3)


wait = WebDriverWait(driver, 60)
freeaddress_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type your address"]')))
freeaddress_textbox.send_keys('Nallur,jaffna')
time.sleep(3)


wait = WebDriverWait(driver, 60)
freebasecate_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')))
freebasecate_textbox.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
freebasecateselect_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')))
freebasecateselect_textbox.send_keys('ATM')
time.sleep(3)

wait = WebDriverWait(driver, 60)
free_close = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="ATM"]')))
free_close.click()
time.sleep(3)

wait = WebDriverWait(driver, 80)
descrip_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]')))
descrip_textbox.send_keys('Best quality')
time.sleep(3)

wait = WebDriverWait(driver, 60)
freecontact_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView')))
freecontact_dropdown.click()
time.sleep(3)

wait = WebDriverWait(driver, 80)
mobileselect_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView[@content-desc="undefined flatlist"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')))
mobileselect_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
mobileno_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 71XXXXXXX"]')))
mobileno_button.send_keys('077886655')
time.sleep(3)

wait = WebDriverWait(driver, 60)
freesave_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
freesave_button.click()
time.sleep(3)

#clear
wait = WebDriverWait(driver, 60)
freedescrip_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]')))
freedescrip_textbox.send_keys('Best quality')
time.sleep(3)

wait = WebDriverWait(driver, 60)
freeclear_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')))
freeclear_button.click()
time.sleep(3)

#fail
wait = WebDriverWait(driver, 60)
freedescrip_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]')))
freedescrip_textbox.send_keys('Best quality')
time.sleep(3)

wait = WebDriverWait(driver, 60)
freesave_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
freesave_button.click()
time.sleep(3)
