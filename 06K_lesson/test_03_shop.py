from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="function")
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Zlata")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Sovik")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("169933")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, '[data-test="total-label"]')))
    result = driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]')
    expected_result = "Total: $58.29"
    assert result.text == expected_result
