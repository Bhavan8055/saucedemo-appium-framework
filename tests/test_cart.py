from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
import time

def test_add_product_to_cart(driver):

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)

    products_page.click_backpack_product()

    product_details_page.add_to_cart()

    cart_count = product_details_page.get_cart_count()

    assert cart_count == "1"