from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(5)

input_str = driver.find_element(By.ID, "username")
input_str.send_keys("tomsmith")
print("Введен логин")

input_str = driver.find_element(By.ID, "password")
input_str.send_keys("SuperSecretPassword!")
print("Введен пароль")

login_buttom = driver.find_element(By.CLASS_NAME, "radius")
login_buttom.click()
print("Пробуем залогиниться")

u_logged = driver.find_element(By.CLASS_NAME, "flash")
print(f'Ура! Мы залогинились: {u_logged.text}')

driver.quit()
