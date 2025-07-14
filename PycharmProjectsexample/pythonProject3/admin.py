from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap ={
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "Testing_device",
  "appium:appPackage": "com.dialus.lk.app",
  "appium:appActivity": "com.dialus.lk.app.MainActivity"
}
driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)


# #more button footer
# wait = WebDriverWait(driver, 60)
# footmore_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
# footmore_button.click()
# time.sleep(3)
#
# #freelisting  button
# wait = WebDriverWait(driver, 60)
# freelist_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Free listing, "]')))
# freelist_button.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# freedis_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select District"]/android.widget.ImageView')))
# freedis_dropdown.click()
# time.sleep(3)
#
#
# wait = WebDriverWait(driver, 60)
# freedisselect_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Jaffna"]')))
# freedisselect_dropdown.click()
# time.sleep(3)
#
#
# wait = WebDriverWait(driver, 60)
# freecity_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Select City"]/android.widget.ImageView')))
# freecity_dropdown.click()
# time.sleep(3)
#
#
# wait = WebDriverWait(driver, 60)
# cityselect_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Analaitivu"]')))
# cityselect_dropdown.click()
# time.sleep(3)
#
#
# wait = WebDriverWait(driver, 60)
# name_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')))
# name_textbox.send_keys('Dial Bank of jaffna')
# time.sleep(3)
#
#
# wait = WebDriverWait(driver, 60)
# address_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type your address"]')))
# address_textbox.send_keys('Nallur,jaffna,4002')
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# cate_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')))
# cate_textbox.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# search_textbox = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type to search..."]')))
# search_textbox.send_keys('Bank')
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# bankclick_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Banks, "]')))
# bankclick_button.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# Des_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Type here"]')))
# Des_button.send_keys('Best bank of jaffna')
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# mobile_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 71XXXXXXX"]')))
# mobile_button.send_keys('776545678')
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# add_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="+"]')))
# add_button.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# contact_dropdown = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.ImageView[2]')))
# contact_dropdown.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# land_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView[@content-desc="undefined flatlist"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView')))
# land_button.click()
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# land1_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="e.g. 021XXXXXXX"]')))
# land1_button.send_keys('0216545678')
# time.sleep(3)
#
# wait = WebDriverWait(driver, 60)
# save_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
# save_button.click()
# time.sleep(3)
# driver.back()


# #addpost button
wait = WebDriverWait(driver, 60)
addpost_icon = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="+"]')))
addpost_icon.click()
time.sleep(3)
#
# #offers
wait = WebDriverWait(driver, 60)
offerhead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
offerhead_button.send_keys('KFC')
time.sleep(2)

wait = WebDriverWait(driver, 60)
offerimage_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]')))
offerimage_button.click()
time.sleep(2)

wait = WebDriverWait(driver, 60)
offerallow_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')))
offerallow_button.click()
time.sleep(2)

wait = WebDriverWait(driver, 60)
offerselectimage_button = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
offerselectimage_button.click()
time.sleep(2)

wait = WebDriverWait(driver, 60)
offerphotocrop_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]')))
offerphotocrop_button.click()
time.sleep(2)


wait = WebDriverWait(driver, 60)
offerdescrip_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
offerdescrip_textbox.send_keys('So spicy')
time.sleep(2)

wait = WebDriverWait(driver, 60)
offerimagelink_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
offerimagelink_textbox.send_keys('www.kfc.com')
time.sleep(2)

wait = WebDriverWait(driver, 60)
offersave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
offersave_button.click()
time.sleep(2)
#
# #Ds collection
wait = WebDriverWait(driver, 60)
DSredio_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="DS Collection"]')))
DSredio_button.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
DShead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
DShead_button.send_keys('kfc')
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSimage_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="JPEG, PNG, JPG up to 2MB"]')))
DSimage_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSselectimage_button = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
DSselectimage_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSphotocrop1_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.dialus.lk.app:id/crop_image_menu_crop"]')))
DSphotocrop1_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSdescrip_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
DSdescrip_textbox.send_keys('No one brand spicy chicken')
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSimagelink_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
DSimagelink_textbox.send_keys('www.kfcc.com')
time.sleep(3)

wait = WebDriverWait(driver, 60)
DSsave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
DSsave_button.click()
time.sleep(3)
driver.back()



wait = WebDriverWait(driver, 60)
footmore_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
footmore_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
login_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login, "]')))
login_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
email_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Enter your email"]')))
email_button.send_keys('admin@gmail.com')
time.sleep(3)

wait = WebDriverWait(driver, 60)
pw_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Enter your password"]')))
pw_button.send_keys('12345678')
time.sleep(3)

wait = WebDriverWait(driver, 60)
inlogin_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Login"]')))
inlogin_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
loginpopup_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')))
loginpopup_button.click()
time.sleep(3)

#business
wait = WebDriverWait(driver, 60)
busi_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Business approval, request, 1"]')))
busi_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
view_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '(//android.widget.TextView[@text="View  "])[1]')))
view_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
accept_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]')))
accept_button.click()
time.sleep(3)


wait = WebDriverWait(driver, 60)
acceptyes_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
acceptyes_button.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
offe_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Offer approval, request, 1"]')))
offe_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
accept_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Accept"]')))
accept_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
acceptyes_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
acceptyes_button.click()
time.sleep(3)
driver.back()

wait = WebDriverWait(driver, 60)
ds_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="DS Collection approval, request, 1"]')))
ds_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
delete_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]')))
delete_button.click()
time.sleep(3)

wait = WebDriverWait(driver, 60)
yes_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Yes"]')))
yes_button.click()
time.sleep(3)
driver.back()


driver.back()
driver.back()

# Navigate to 'Home'
wait = WebDriverWait(driver, 60)
home_button = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text=""]')))
home_button.click()


