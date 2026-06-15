from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.review_order_page import ReviewOrderPage
from pages.order_success_page import OrderSuccessPage

def test_checkout_process(driver):

    login_page = LoginPage(driver)

    # Login first
    login_page.navigate_to_login_screen()
    login_page.login("bod@example.com", "10203040")

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    payment_page = PaymentPage(driver)
    review_order_page = ReviewOrderPage(driver)

    products_page.click_backpack_product()
    product_details_page.add_to_cart()
    cart_page.open_cart()

    checkout_page.proceed_checkout()
    checkout_page.enter_shipping_details()
    checkout_page.continue_to_payment()

    payment_page.enter_payment_details()
    payment_page.review_order()

    review_order_page.place_order()

    success_page = OrderSuccessPage(driver)
    assert success_page.is_order_successful()

    print("Order placed successfully")