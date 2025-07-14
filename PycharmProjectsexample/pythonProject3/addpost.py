from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_cap = {
  "appium:automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:deviceName": "addpost",
  "appium:appPackage": "com.thileepan.Add",
  "appium:appActivity": "com.thileepan.Add.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723',desired_cap)

#offers
wait = WebDriverWait(driver, 60)
offerhead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
offerhead_button.send_keys('Sana')
time.sleep(3)


#offer image select text box
wait = WebDriverWait(driver, 60)
offerimage_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="Tap to upload your image"]')))
offerimage_button.click()
time.sleep(3)


#image allow function in gallery
wait = WebDriverWait(driver, 60)
offerallow_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')))
offerallow_button.click()
time.sleep(3)


#select the image
wait = WebDriverWait(driver, 60)
offerselectimage_button = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
offerselectimage_button.click()
time.sleep(3)


# crop the image
wait = WebDriverWait(driver, 60)
offerphotocrop1_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')))
offerphotocrop1_button.click()
time.sleep(3)


#description text box click & type
wait = WebDriverWait(driver, 60)
offerdescrip_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
offerdescrip_textbox.send_keys('view the dialus web')
time.sleep(3)


# add image link in text box
wait = WebDriverWait(driver, 60)
offerimagelink_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
offerimagelink_textbox.send_keys('https//dialus')
time.sleep(3)


# save the data (offer)
wait = WebDriverWait(driver, 60)
offersave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
offersave_button.click()
time.sleep(3)


#enter the heading offer heading text box
wait = WebDriverWait(driver, 60)
offerhead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
offerhead_button.send_keys('Sana jeya')
time.sleep(3)


# click the clear button
wait = WebDriverWait(driver, 60)
offerclear_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')))
offerclear_button.click()
time.sleep(3)


#fail
#offers
#enter the heading offer heading text box
wait = WebDriverWait(driver, 60)
offerhead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
offerhead_button.send_keys('Sana')
time.sleep(3)


# save the data (offer)
wait = WebDriverWait(driver, 60)
offersave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
offersave_button.click()
time.sleep(3)


#Ds collection
# click ds redio button
wait = WebDriverWait(driver, 60)
DSredio_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="DS Collection"]')))
DSredio_button.click()
time.sleep(3)


# enter ds heading in heading text box & add heading
wait = WebDriverWait(driver, 60)
DShead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
DShead_button.send_keys('festival')
time.sleep(3)

# click ds image text box
wait = WebDriverWait(driver, 60)
DSimage_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="Tap to upload your image"]')))
DSimage_button.click()
time.sleep(3)


#select the image in gellary
wait = WebDriverWait(driver, 60)
DSselectimage_button = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
DSselectimage_button.click()
time.sleep(3)

# crop the image
wait = WebDriverWait(driver, 60)
DSphotocrop1_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')))
DSphotocrop1_button.click()
time.sleep(3)


# click ds description text box & add data
wait = WebDriverWait(driver, 60)
DSdescrip_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your description"]')))
DSdescrip_textbox.send_keys('view the dialus web')
time.sleep(3)


# add ds image link
wait = WebDriverWait(driver, 60)
DSimagelink_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
DSimagelink_textbox.send_keys('https//dialus')
time.sleep(3)

# click save button
wait = WebDriverWait(driver, 60)
DSsave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
DSsave_button.click()
time.sleep(3)

# enter ds heading in heading text box & add heading
wait = WebDriverWait(driver, 60)
DShead_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')))
DShead_button.send_keys('festval')
time.sleep(3)


# click clear button
wait = WebDriverWait(driver, 60)
DSclear_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')))
DSclear_button.click()
time.sleep(3)


#advertisement
#click redio button
wait = WebDriverWait(driver, 60)
Adsredio_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="Advertisement"]')))
Adsredio_button.click()
time.sleep(3)

#Add the name
wait = WebDriverWait(driver, 80)
Adsname_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')))
Adsname_button.send_keys('keels')
time.sleep(3)


# add the logo
wait = WebDriverWait(driver, 80)
Adslogo_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Tap to upload your image"]')))
Adslogo_button.click()
time.sleep(3)


# select the image in gellary
wait = WebDriverWait(driver, 80)
Adsselectimage_button = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]')))
Adsselectimage_button.click()
time.sleep(3)

#crop the image
wait = WebDriverWait(driver, 80)
Adsphotocrop1_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]')))
Adsphotocrop1_button.click()
time.sleep(3)

# aa the image link
wait = WebDriverWait(driver, 80)
Adsimagelink_textbox = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')))
Adsimagelink_textbox.send_keys('https//dialus')
time.sleep(3)


# click save button
wait = WebDriverWait(driver, 60)
Adssave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
Adssave_button.click()
time.sleep(3)


# add the name
wait = WebDriverWait(driver, 60)
Adsname_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.EditText[@text="Type your name"]')))
Adsname_button.send_keys('keels')
time.sleep(3)


# click clear button
wait = WebDriverWait(driver, 60)
Adsclear_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')))
Adsclear_button.click()
time.sleep(3)

#advertisement
# click ads redio button
wait = WebDriverWait(driver, 60)
Adsredio_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@text="Advertisement"]')))
Adsredio_button.click()
time.sleep(3)

#click save button
wait = WebDriverWait(driver, 60)
Adssave_button = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')))
Adssave_button.click()
time.sleep(3)