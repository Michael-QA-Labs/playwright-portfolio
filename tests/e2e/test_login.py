import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_valid_login(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        expect(page).to_have_url(InventoryPage.URL)

    def test_locked_out_user(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("locked_out_user", "secret_sauce")
        expect(login.error_message).to_be_visible()
        expect(login.error_message).to_contain_text("locked out")

    def test_invalid_password(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "wrong_password")
        expect(login.error_message).to_be_visible()

    def test_empty_credentials(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("", "")
        expect(login.error_message).to_be_visible()
        expect(login.error_message).to_contain_text("Username is required")
