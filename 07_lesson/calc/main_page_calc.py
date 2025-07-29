from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def button_calc(self, button):
        self.driver.find_element(By.XPATH, f"//*[text()='{button}']").click()

    def wait_delay(self, value_delay, result_calc):
        WebDriverWait(self.driver, value_delay).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), str(result_calc)))

    def result_calc(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(result)
