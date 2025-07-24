from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
driver.implicitly_wait(5)

input_str = driver.find_element(By.TAG_NAME, "input")
input_str.send_keys("Sky")
print("Пропечатано Sky")

input_str.clear()
print("Поле очищено")

input_str.send_keys("Pro")
print("Пропечатано Pro")

driver.quit()
