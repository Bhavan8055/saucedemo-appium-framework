from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SearchDetailsPage(BasePage):
    # Finding the elements safely via structural XPath assignments
    FIRST_PRODUCT_TITLE = (AppiumBy.XPATH, "(//*[@resource-id='com.saucelabs.mydemoapp.android:id/titleTV'])[1]")
    PRODUCT_PRICE = (AppiumBy.XPATH, "//*[@resource-id='com.saucelabs.mydemoapp.android:id/priceTV']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_first_catalog_item(self):
        self.logger.info("Tapping the first item title in the catalog using strict index XPath...")
        self.click_element(*self.FIRST_PRODUCT_TITLE)

    def is_price_displayed(self):
        self.logger.info("Checking if the product price displays via XPath validation...")
        return self.is_element_displayed(*self.PRODUCT_PRICE)