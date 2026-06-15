from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_ICON = (AppiumBy.ACCESSIBILITY_ID, "home_search")
    PROFILE_ICON = (AppiumBy.ACCESSIBILITY_ID, "home_profile")
    FAVORITES_ICON = (AppiumBy.ACCESSIBILITY_ID, "home_favorites")
    WATCHLIST_ICON = (AppiumBy.ACCESSIBILITY_ID, "home_watchlist")
    LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "home_logout")
    HOME_TITLE = (AppiumBy.ACCESSIBILITY_ID, "home_title")

    def is_displayed(self) -> bool:
        return self.is_displayed(self.HOME_TITLE)

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def open_profile(self):
        self.click(self.PROFILE_ICON)

    def open_favorites(self):
        self.click(self.FAVORITES_ICON)

    def open_watchlist(self):
        self.click(self.WATCHLIST_ICON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
