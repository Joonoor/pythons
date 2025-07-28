from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="function")
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calc(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    driver.find_element(By.XPATH, "//*[text()='7']").click()
    driver.find_element(By.XPATH, "//*[text()='+']").click()
    driver.find_element(By.XPATH, "//*[text()='8']").click()
    start_time = time.time()
    driver.find_element(By.XPATH, "//*[text()='=']").click()
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    end_time = time.time()
    elapsed_time = end_time - start_time

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    expected_result = "15"
    expected_delay = 45

    assert result == expected_result, f"Резултат {result} != {expected_result}"
    assert abs(elapsed_time - expected_delay) < 2, f"Время {
        elapsed_time:.2f} не близко к {expected_delay} сек"
