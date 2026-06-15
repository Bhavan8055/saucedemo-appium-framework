from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class MovieDetailsPage(BasePage):
    MOVIE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "details_movie_title")
    ADD_TO_FAVORITES = (AppiumBy.ACCESSIBILITY_ID, "details_add_favorites")
    REMOVE_FROM_FAVORITES = (AppiumBy.ACCESSIBILITY_ID, "details_remove_favorites")
    ADD_TO_WATCHLIST = (AppiumBy.ACCESSIBILITY_ID, "details_add_watchlist")
    FAVORITES_STATUS = (AppiumBy.ACCESSIBILITY_ID, "details_favorite_status")
    WATCHLIST_STATUS = (AppiumBy.ACCESSIBILITY_ID, "details_watchlist_status")

    def get_movie_title(self) -> str:
        return self.get_text(self.MOVIE_HEADER)

    def add_to_favorites(self):
        self.click(self.ADD_TO_FAVORITES)

    def remove_from_favorites(self):
        self.click(self.REMOVE_FROM_FAVORITES)

    def add_to_watchlist(self):
        self.click(self.ADD_TO_WATCHLIST)

    def is_favorite(self) -> bool:
        return "favorite" in self.get_text(self.FAVORITES_STATUS).lower()

    def is_in_watchlist(self) -> bool:
        return "watchlist" in self.get_text(self.WATCHLIST_STATUS).lower()
