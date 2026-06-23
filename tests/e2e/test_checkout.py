import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:

    def test_full_purchase_flow(self, page: Page):
        # Login
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        expect(page).to_have_url(InventoryPage.URL)

        # Add item to cart
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()
        expect(page).to_have_url(CartPage.URL)

        # Verify item in cart
        cart = CartPage(page)
        expect(cart.cart_items).to_have_count(1)

        # Checkout
        cart.checkout()
        expect(page).to_have_url(CheckoutPage.STEP_ONE_URL)

        # Fill info
        checkout = CheckoutPage(page)
        checkout.fill_info("Michael", "Garcia", "10701")
        expect(page).to_have_url(CheckoutPage.STEP_TWO_URL)

        # Finish
        checkout.finish()
        expect(page).to_have_url(CheckoutPage.COMPLETE_URL)
        expect(checkout.confirmation_header).to_contain_text("Thank you")

    def test_checkout_missing_info(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.checkout()

        checkout = CheckoutPage(page)
        checkout.fill_info("", "", "")
        error = page.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("First Name is required")
