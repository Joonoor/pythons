from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def authorization(self, login, password):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
        login_input = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        login_input.clear()
        login_input.send_keys(login)

        password_input = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.clear()
        password_input.send_keys(password)

    def login_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#login-button")))
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
