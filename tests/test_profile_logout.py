import pytest
from pages.home_page import HomePage
from pages.search_details_page import SearchDetailsPage
from pages.movie_details_page import MovieDetailsPage
from pages.profile_page import ProfilePage
from utilities.data_reader import load_test_data


@pytest.mark.regression
@pytest.mark.parametrize("profile_data", load_test_data("profile_update"))
def test_profile_update_and_logout(driver, profile_data):
    """Verify that a user can update their profile and log out successfully."""
    home_page = HomePage(driver)
    home_page.open_profile()

    profile_page = ProfilePage(driver)
    profile_page.update_profile(
        profile_data["name"],
        profile_data["email"],
        profile_data["bio"],
    )
    assert profile_page.is_profile_updated(), "Profile should be updated successfully"

    home_page.logout()
    assert not home_page.is_displayed(), "User should be logged out and home screen should not be visible"
