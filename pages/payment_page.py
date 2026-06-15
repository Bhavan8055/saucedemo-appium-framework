from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class PaymentPage(BasePage):

    NAME_ON_CARD = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/nameET"
    )

    CARD_NUMBER = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cardNumberET"
    )

    EXPIRY_DATE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/expirationDateET"
    )

    SECURITY_CODE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/securityCodeET"
    )

    REVIEW_ORDER = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/paymentBtn"
    )

    def enter_payment_details(self):
        self.input_text(*self.NAME_ON_CARD, "Bhavan Test")
        self.input_text(*self.CARD_NUMBER, "4111111111111111")
        self.input_text(*self.EXPIRY_DATE, "12/30")
        self.input_text(*self.SECURITY_CODE, "123")

    def review_order(self):
        self.click_element(*self.REVIEW_ORDER)