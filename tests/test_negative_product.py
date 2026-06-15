from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

def test_wrong_product_verification(driver):

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)

    products_page.click_backpack_product()
    product_details_page.add_to_cart()
    cart_page.open_cart()

    # Intentional failure
    assert cart_page.is_product_present() == False, \
        "Intentional failure: Product is actually present in cart"