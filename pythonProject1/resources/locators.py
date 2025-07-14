from appium.webdriver.common.mobileby import MobileBy

class HomeLocators:
    MORE_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="More"]')
    PLUS_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="+"]')
    HOSPITALS = (MobileBy.XPATH, '//android.widget.TextView[@text="hospitals"]')
    COURIER = (MobileBy.XPATH, '//android.widget.TextView[@text="Courier"]')
    LEASING = (MobileBy.XPATH, '//android.widget.TextView[@text="Leasing"]')
    BANKS = (MobileBy.XPATH, '//android.widget.TextView[@text="Banks"]')
    ATM = (MobileBy.XPATH, '//android.widget.TextView[@text="ATM"]')
    SUPERMARKETS = (MobileBy.XPATH, '//android.widget.TextView[@text="Supermarkets"]')
    RESTAURANT = (MobileBy.XPATH, '//android.widget.TextView[@text="Restaurant"]')

class MoreLocators:
    ABOUT_US_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="About us, "]')
    CONTACT_US_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Contact us, "]')


class AboutUsLocators:
    ABOUT_US_TEXT = (MobileBy.XPATH, '//android.widget.TextView[@text="About Us"]')

class ContactUsLocators:
    CONTACT_US_TEXT = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Contact us, "]')

class AddPostLocators:
    ADD_POST_HEADER = (MobileBy.XPATH, '//android.widget.TextView[@text="Add Post"]')  # ← Example
    # Radio buttons for category selection
    OFFERS_RADIO = (MobileBy.XPATH, '//android.widget.TextView[@text="Offers"]')

    # Input fields
    MOBILE_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your mobile number"]')
    NAME_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your name"]')
    WORK_POSITION_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your work position"]')
    EMAIL_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your email"]')
    # START_DATE_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Select start date"]')
    # END_DATE_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Select end date"]')
    # HEADING_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Type your heading"]')
    # IMAGE_LINK_INPUT = (MobileBy.XPATH, '//android.widget.EditText[@text="Add your image link"]')

    # Image upload box (if needed for interaction)
    # IMAGE_UPLOAD_BOX = (MobileBy.XPATH, '//android.widget.ImageView[contains(@content-desc, "upload")]')

    # Buttons
    SAVE_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Save"]')
    CLEAR_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')

    # DS form
    DS_COLLECTION_RADIO = (MobileBy.XPATH, '//android.widget.TextView[@text="DS Collection"]')

    ADVERTISEMENT_RADIO = (MobileBy.XPATH, '//android.widget.TextView[@text="Advertisement"]')

    # FreeListingform
    class FreeListingLocators:
        MORE_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="More"]')
        FREE_LISTING_BUTTON = (MobileBy.ANDROID_UIAUTOMATOR, '//android.view.ViewGroup[@content-desc="Free listing, "]')
        DISTRICT_DROPDOWN = (MobileBy.ID, '//android.view.ViewGroup[@content-desc="Select District"]/android.widget.ImageView')
        DISTRICT_OPTION = (MobileBy.ANDROID_UIAUTOMATOR, '//android.widget.TextView[@text="Jaffna"]')  # Change as needed
        CITY_DROPDOWN = (MobileBy.ID, '//android.view.ViewGroup[@content-desc="Select City"]/android.widget.ImageView')
        CITY_OPTION = (MobileBy.ANDROID_UIAUTOMATOR, '//android.widget.TextView[@text="Analaitivu"]')
        NAME_INPUT = (MobileBy.ID, '//android.widget.EditText[@text="Type your name"]')
        ADDRESS_INPUT = (MobileBy.ID, '//android.widget.EditText[@text="Type your address"]')
        BASE_CATEGORY_FIELD = (MobileBy.ID, '//android.widget.EditText[@text="Type to search..."]')
        BASE_CATEGORY1_INPUT = (MobileBy.ID, '//android.widget.EditText[@text="Type to search..."]')
        BASE_CATEGORY1_CLOSE = (MobileBy.ID, '//android.widget.TextView[@text="Close"]')
        DESCRIPTION_INPUT = (MobileBy.ID, '//android.widget.EditText[@text="Type here"]')
        PHONE_INPUT = (MobileBy.ID, '//android.widget.EditText[@text="e.g. 71XXXXXXX"]')
        SAVE_BUTTON = (MobileBy.ID, '//android.view.ViewGroup[@content-desc="Save"]')





