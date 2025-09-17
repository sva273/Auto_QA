import pytest
from lesson_9.pages.login_page import LoginPage
from lesson_9.pages.inventory_page import InventoryPage
from lesson_9.pages.cart_page import CartPage
from lesson_9.pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
class TestAllItemsCost:
    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def test_all_items_cost_are_correct(self):
        # Авторизация
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

        # Цены товаров
        items_cost_from_inventory = [
            self.inventory_page.get_item_price("Sauce Labs Backpack"),
            self.inventory_page.get_item_price("Sauce Labs Onesie"),
            self.inventory_page.get_item_price("Sauce Labs Bolt T-Shirt")
        ]

        # Добавление товаров в корзину
        for item in ["Sauce Labs Backpack", "Sauce Labs Onesie", "Sauce Labs Bolt T-Shirt"]:
            self.inventory_page.add_item_to_cart(item)

        # Переход в корзину и оформление заказа
        self.inventory_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information("Slava", "Schwab", "09210")
        self.checkout_page.continue_checkout()
        total_price = self.checkout_page.get_total_price()
        assert total_price == "$58.29", f"Итоговая сумма неверна: {total_price}"

