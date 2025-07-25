from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 20)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))


img = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute('src')

print(img)

driver.quit()
