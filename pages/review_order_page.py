from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ReviewOrderPage(BasePage):

    PLACE_ORDER_BUTTON = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/paymentBtn"
    )

    def place_order(self):
        self.click_element(*self.PLACE_ORDER_BUTTON)