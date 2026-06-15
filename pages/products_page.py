from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ProductsPage(BasePage):

    PRODUCT_IMAGE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/productIV"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def click_backpack_product(self):
        self.click_element(*self.PRODUCT_IMAGE)