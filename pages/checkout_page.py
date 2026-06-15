from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CheckoutPage(BasePage):

    PROCEED_TO_CHECKOUT = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cartBt"
    )

    FULL_NAME = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/fullNameET"
    )

    ADDRESS = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/address1ET"
    )

    CITY = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cityET"
    )

    ZIP_CODE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/zipET"
    )

    COUNTRY = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/countryET"
    )

    TO_PAYMENT = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/paymentBtn"
    )

    def proceed_checkout(self):
        self.click_element(*self.PROCEED_TO_CHECKOUT)

    def enter_shipping_details(self):
        self.input_text(*self.FULL_NAME, "Bhavan")
        self.input_text(*self.ADDRESS, "123 Test Street")
        self.input_text(*self.CITY, "Bangalore")
        self.input_text(*self.ZIP_CODE, "560001")
        self.input_text(*self.COUNTRY, "India")

    def continue_to_payment(self):
        self.click_element(*self.TO_PAYMENT)