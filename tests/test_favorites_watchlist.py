import pytest
from pages.home_page import HomePage
from pages.search_details_page import SearchDetailsPage
from pages.movie_details_page import MovieDetailsPage
from utilities.data_reader import load_test_data


@pytest.mark.regression
@pytest.mark.parametrize("data", load_test_data("search"))
def test_add_and_remove_favorites_and_watchlist(driver, data):
    """Verify that movies can be added to favorites and watchlist, then removed from favorites."""
    home_page = HomePage(driver)
    home_page.open_search()

    search_page = SearchPage(driver)
    search_page.search_movie(data["movie_name"])
    assert search_page.select_movie(data["movie_name"]), "Movie should be found in search results"

    details_page = MovieDetailsPage(driver)
    details_page.add_to_favorites()
    assert details_page.is_favorite(), "Movie should be marked as favorite"

    details_page.add_to_watchlist()
    assert details_page.is_in_watchlist(), "Movie should be added to the watchlist"

    details_page.remove_from_favorites()
    assert not details_page.is_favorite(), "Movie should be removed from favorites"
