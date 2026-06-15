import pytest
import time
from pages.search_details_page import SearchDetailsPage

@pytest.mark.usefixtures("driver")
class TestCatalogSearchDetails:
    def test_search_and_view_item_details(self):
        # Give the emulator 3 seconds to fully settle into the app screen
        time.sleep(3)
        
        search_details = SearchDetailsPage(self.driver)
        
        # 1. Click the top-most visible item card via ID
        search_details.select_first_catalog_item()
        
        # 2. Verify the individual price details populate on the next screen
        assert search_details.is_price_displayed() == True, "Product price information failed to populate."