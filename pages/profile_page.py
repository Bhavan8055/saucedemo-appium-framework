from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProfilePage(BasePage):
    NAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "profile_name")
    EMAIL_FIELD = (AppiumBy.ACCESSIBILITY_ID, "profile_email")
    BIO_FIELD = (AppiumBy.ACCESSIBILITY_ID, "profile_bio")
    UPDATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "profile_update")
    SAVE_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "profile_saved")

    def update_profile(self, name: str, email: str, bio: str):
        self.send_keys(self.NAME_FIELD, name)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.BIO_FIELD, bio)
        self.click(self.UPDATE_BUTTON)

    def is_profile_updated(self) -> bool:
        return self.is_displayed(self.SAVE_MESSAGE)
