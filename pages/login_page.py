from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    # Precise locators targeting interactable widgets directly
    MENU_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='View menu' or @resource-id='com.saucelabs.mydemoapp.android:id/menuIV']")
    LOGIN_MENU_ITEM = (AppiumBy.XPATH, "//*[@content-desc='Login Menu Item' or @text='Log In']")
    
    # Strictly targeting the EditText boxes to prevent clicking static labels
    USERNAME_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.saucelabs.mydemoapp.android:id/nameET']")
    PASSWORD_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.saucelabs.mydemoapp.android:id/passwordET']")
    LOGIN_BUTTON = (AppiumBy.XPATH, "//*[@content-desc='Tap to login with given credentials' or @text='Log In']")
    
    PRODUCTS_HEADER = (AppiumBy.XPATH, "//*[@text='Products']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_screen(self):
        self.click_element(*self.MENU_BUTTON)
        self.click_element(*self.LOGIN_MENU_ITEM)

    def login(self, username, password):
        self.input_text(*self.USERNAME_FIELD, username)
        self.input_text(*self.PASSWORD_FIELD, password)
        self.click_element(*self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_element_displayed(*self.PRODUCTS_HEADER)