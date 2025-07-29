from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChecoutTwoPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def result_total(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '[data-test="total-label"]')))
        result = self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]')
        return result.text
