from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_item_price(self, item_name):
        xpath = f"//div[@class='inventory_item' and .//div[text()='{item_name}']]//div[@class='inventory_item_price']"
        return self.driver.find_element(By.XPATH, xpath).text

    def add_item_to_cart(self, item_name):
        xpath = f"//div[@class='inventory_item' and .//div[text()='{item_name}']]//button"
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
