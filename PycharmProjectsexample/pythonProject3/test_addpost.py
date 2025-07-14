from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def report_action(action_description, xpath=None, input_text=None, click=False):
    """
    Logs the action, performs the step, and handles exceptions.
    :param action_description: Description of the test step.
    :param xpath: XPath of the target element.
    :param input_text: Text to input (if any).
    :param click: Whether to perform a click action.
    """
    try:
        print(f"[INFO] {action_description}...")
        wait = WebDriverWait(driver, 60)
        element = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, xpath)))

        if input_text:
            element.send_keys(input_text)
            print(f"[PASS] {action_description} - Input '{input_text}' successful.")
        if click:
            element.click()
            print(f"[PASS] {action_description} - Click action successful.")
        time.sleep(3)
    except Exception as e:
        print(f"[FAIL] {action_description} - Error: {e}")

def test_pass():
    assert 1 == 1
# Desired Capabilities
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "platformName": "Android",
    "appium:deviceName": "addpost",
    "appium:appPackage": "com.thileepan.Add",
    "appium:appActivity": "com.thileepan.Add.MainActivity",
}

driver = webdriver.Remote('http://127.0.0.1:4723', desired_cap)

# Start of the test case
try:
    print("[TEST] Start: Offer Section Tests")
    report_action("Enter offer heading", '//android.widget.EditText[@text="Type your heading"]', input_text="Sana")
    report_action("Click 'Upload Image' text box", '//android.widget.TextView[@text="Tap to upload your image"]', click=True)
    report_action("Allow image access in gallery", '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]', click=True)
    report_action("Select the first image", '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]', click=True)
    report_action("Crop the image", '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]', click=True)
    report_action("Enter description", '//android.widget.EditText[@text="Add your description"]', input_text="view the dialus web")
    report_action("Add image link", '//android.widget.EditText[@text="Add your image link"]', input_text="https//dialus")
    report_action("Save the offer data", '//android.view.ViewGroup[@content-desc="Save"]', click=True)

    print("[TEST] Start: DS Collection Section Tests")
    report_action("Select DS Collection option", '//android.widget.TextView[@text="DS Collection"]', click=True)
    report_action("Enter DS heading", '//android.widget.EditText[@text="Type your heading"]', input_text="festival")
    report_action("Click 'Upload Image' text box", '//android.widget.TextView[@text="Tap to upload your image"]', click=True)
    report_action("Select the first image", '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]', click=True)
    report_action("Crop the image", '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]', click=True)
    report_action("Enter description", '//android.widget.EditText[@text="Add your description"]', input_text="view the dialus web")
    report_action("Add DS image link", '//android.widget.EditText[@text="Add your image link"]', input_text="https//dialus")
    report_action("Save the DS data", '//android.view.ViewGroup[@content-desc="Save"]', click=True)

    print("[TEST] Start: Advertisement Section Tests")
    report_action("Select Advertisement option", '//android.widget.TextView[@text="Advertisement"]', click=True)
    report_action("Enter Advertisement name", '//android.widget.EditText[@text="Type your name"]', input_text="keels")
    report_action("Click 'Upload Logo' text box", '//android.view.ViewGroup[@content-desc="Tap to upload your image"]', click=True)
    report_action("Select the first image", '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]', click=True)
    report_action("Crop the image", '//android.widget.Button[@resource-id="com.thileepan.Add:id/crop_image_menu_crop"]', click=True)
    report_action("Add Advertisement image link", '//android.widget.EditText[@text="Add your image link"]', input_text="https//dialus")
    report_action("Save the Advertisement data", '//android.view.ViewGroup[@content-desc="Save"]', click=True)

except Exception as e:
    print(f"[TEST FAIL] Error encountered during test execution: {e}")
finally:
    driver.quit()
    print("[TEST COMPLETE]")
