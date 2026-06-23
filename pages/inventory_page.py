from playwright.sync_api import Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart(self, item_name: str):
        self.page.get_by_text("Add to cart", exact=False).first.click()

    def go_to_cart(self):
        self.cart_icon.click()
