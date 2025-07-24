from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")
driver.implicitly_wait(5)

blue_bottom = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_bottom.click()
print("Синия кнопка была нажата")

driver.quit()
