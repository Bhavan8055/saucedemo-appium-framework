from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ProductDetailsPage(BasePage):

    ADD_TO_CART_BUTTON = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cartBt"
    )

    CART_BADGE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cartTV"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.logger.info("Clicking Add To Cart button")
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        return self.get_element_text(*self.CART_BADGE)