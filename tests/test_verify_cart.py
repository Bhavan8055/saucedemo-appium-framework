from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


def test_verify_product_in_cart(driver):

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)

    # Select Product
    products_page.click_backpack_product()

    # Add To Cart
    product_details_page.add_to_cart()

    # Open Cart
    cart_page.open_cart()

    # Verify Product Exists
    assert cart_page.is_product_present()

    print("Product verified successfully in cart")