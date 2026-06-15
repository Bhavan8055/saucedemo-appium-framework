from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class OrderSuccessPage(BasePage):

    SUCCESS_MESSAGE = (
        AppiumBy.XPATH,
        "//*[contains(@text,'Thank')]"
    )

    BACK_HOME_BUTTON = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/shoopingBt"
    )

    def is_order_successful(self):
        return self.is_element_displayed(*self.SUCCESS_MESSAGE)

    def go_back_home(self):
        self.click_element(*self.BACK_HOME_BUTTON)