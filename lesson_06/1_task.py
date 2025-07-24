from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 20)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CLASS_NAME, "btn-primary").click()

element = waiter.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))

print(element.text)

driver.quit()
