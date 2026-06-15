import pytest
from pages.products_page import ProductsPage
from utilities.logger import get_logger

@pytest.mark.usefixtures("driver")
class TestProductsCatalog:
    logger = get_logger()

    def test_verify_catalog_page_loads(self,driver):
        self.logger.info("Executing: test_verify_catalog_page_loads")
        products_page = ProductsPage(driver)
        
        # Verify landing page displays correctly
        assert products_page.is_products_header_displayed() == True, "Products catalog header was not displayed!"
        
        # Verify text value matches
        header_text = products_page.get_header_title()
        assert header_text == "Products", f"Expected header text 'Products', but found: {header_text}"
        
        self.logger.info("Catalog page successfully verified via Page Object Model architecture!")