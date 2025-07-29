from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="function")
def driver():
    driver_path = r"B:\zagruzki\edgedriver_win64\msedgedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_color_zip_code(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(By.CLASS_NAME, "btn-outline-primary").click()
    waiter = WebDriverWait(driver, 10)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")))
    zip_bg_color = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_bg_color == "rgba(248, 215, 218, 1)"


def test_color_green_input(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(By.CLASS_NAME, "btn-outline-primary").click()
    waiter = WebDriverWait(driver, 10)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")))
    green_input = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(green_input) == 9
