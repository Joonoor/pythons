from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self, item_name):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item")))
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        item_found = False

        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == item_name:
                add_button = item.find_element(
                    By.CSS_SELECTOR, "button.btn_inventory")
                add_button.click()
                item_found = True
                break
        if not item_found:
            raise Exception(f"Товар с названием '{item_name}' не найден")
