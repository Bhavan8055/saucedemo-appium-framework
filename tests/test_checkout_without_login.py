from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest
from selenium.common.exceptions import TimeoutException

def test_checkout_without_login(driver):

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    products_page.click_backpack_product()
    product_details_page.add_to_cart()
    cart_page.open_cart()

    checkout_page.proceed_checkout()

    try:
        checkout_page.enter_shipping_details()
    except TimeoutException:
        pytest.fail(
            "Checkout failed because the user was not logged in. "
            )