from playwright.sync_api import Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def checkout(self):
        self.checkout_button.click()
