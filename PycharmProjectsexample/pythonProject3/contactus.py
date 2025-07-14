from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Testing_device",
  "appium:appPackage": "com.thivja.myapp",
  "appium:appActivity": "com.thivja.myapp.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)
#contactus form


wait = WebDriverWait(driver, 60)
name_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your name"]')))
name_textbox.send_keys('Sana')
time.sleep(3)

wait = WebDriverWait(driver, 60)
email_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your email address"]')))
email_textbox.send_keys('sana@gmail.com')
time.sleep(3)

wait = WebDriverWait(driver, 60)
writehere_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your text here..."]')))
writehere_textbox.send_keys('hello sana')
time.sleep(3)

wait = WebDriverWait(driver, 60)
send_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Send"]')))
send_button.click()
time.sleep(3)


#fail
wait = WebDriverWait(driver, 60)
name_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your name"]')))
name_textbox.send_keys()
time.sleep(3)

wait = WebDriverWait(driver, 60)
email_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your email address"]')))
email_textbox.send_keys('sana@gmail.com')
time.sleep(3)

wait = WebDriverWait(driver, 60)
writehere_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your text here..."]')))
writehere_textbox.send_keys('hello sana')
time.sleep(3)

wait = WebDriverWait(driver, 60)
send_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Send"]')))
send_button.click()
time.sleep(3)

#fail
wait = WebDriverWait(driver, 80)
name_textbox3 = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your name"]')))
name_textbox3.send_keys('San')
time.sleep(3)

wait = WebDriverWait(driver, 80)
email_textbox4 = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your email address"]')))
email_textbox4.send_keys('sanagmail')
time.sleep(3)

wait = WebDriverWait(driver, 80)
writehere_textbox5 = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Your text here..."]')))
writehere_textbox5.send_keys('hello san')
time.sleep(3)

wait = WebDriverWait(driver, 80)
send_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Send"]')))
send_button.click()
time.sleep(3)




