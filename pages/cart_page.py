from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CartPage(BasePage):

    CART_ICON = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/cartIV"
    )

    PRODUCT_NAME = (
        AppiumBy.XPATH,
        "//*[@text='Sauce Labs Backpack']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_cart(self):
        self.click_element(*self.CART_ICON)

    def is_product_present(self):
        return self.is_element_displayed(*self.PRODUCT_NAME)