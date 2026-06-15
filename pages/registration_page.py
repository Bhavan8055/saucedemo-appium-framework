from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "register_name")
    EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, "register_email")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "register_password")
    CONFIRM_PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "register_confirm_password")
    REGISTER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "register_button")
    SUCCESS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "register_success")

    def register(self, name: str, email: str, password: str, confirm_password: str):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.REGISTER_BUTTON)

    def is_registration_successful(self) -> bool:
        return self.is_displayed(self.SUCCESS_MESSAGE)
