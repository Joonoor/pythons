# сайт Example Domain
#  вывести заголовок станицы в консоль
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

print(f'Заголовок страницы: {driver.title}')

driver.quit()

# сайт питон
# вывести и нажать кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

driver.find_element(By.LINK_TEXT, "Donate").click()

driver.quit()

# сайт гугл поисковая строка
# ввести строку и нажать гугл
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Найти строку поиска и ввести "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")

# Нажать Enter для выполнения поиска
search_box.send_keys(Keys.RETURN)

driver.quit()
