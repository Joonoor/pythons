from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage():

    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver - объект драйвера Selenium.

        В конструктор вшито открытие страницы калькулятора.
        """
        self.driver = driver
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки '{value}' для калькулятора")
    def delay(self, value):
        """
        Устанавливает время задержки перед началом операции на калькуляторе.

        :param delay: int - время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)

    @allure.step("Нажатие кнопки '{button}")
    def button_calc(self, button):
        """
        Нажимает на кнопку на калькуляторею

        :param button: str - текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, f"//*[text()='{button}']").click()

    @allure.step("Ожидание появления результата '{result_calc}'.")
    def wait_delay(self, value_delay, result_calc):
        """
        Ожидает появления ожидаемого результата калькулятора на экране.

        :param value_delay: int - время ожидания результата.
         Установленное время методом delay + 1 секунда.
        :param result_calc: str - ожидаемый результат.
        """
        WebDriverWait(self.driver, value_delay).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), str(result_calc)))

    @allure.step("Получение результата с экрана")
    def result_calc(self):
        """
        Возвращает фактический результат с экрана калькулятора.

        :return: int - число результата на экране каалькулятора.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(result)
