from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from main_page_calc import MainPage
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для открытия и закрытия драйвера.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description(
    "Тест проверяет корректность задержки и вычислительной работы.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
def test_calc(driver):
    """
    Тест проверяет работу калькулятора с задданными операциями.

    :param driver: WebDriver - объект драйвера, переданный фикстурой.
    """

    with allure.step("Фиксация ожидаемых результатов"):
        expected_result = 15
        expected_delay = 45

    with allure.step(f"Открытие калькулятора в {driver}"):
        main_page = MainPage(driver)

    with allure.step("Установка задержки в секундах"):
        main_page.delay(45)

    with allure.step("Задаём вычислительную операцию"):
        main_page.button_calc('7')
        main_page.button_calc('+')
        main_page.button_calc('8')

    with allure.step("Фиксируем начало задержки"):
        start_time = time.time()

    with allure.step("Запускаем вычислительную работу"):
        main_page.button_calc("=")
        main_page.wait_delay(46, 15)

    with allure.step("Фиксируем окончание вычислительной работы"):
        end_time = time.time()
        elapsed_time = end_time - start_time

    with allure.step("Фиксируем результат вычислительной работы"):
        as_is_num = main_page.result_calc()

    with allure.step("Проверка результата"):
        assert as_is_num == expected_result, f"Резултат {as_is_num} != {
            expected_result}"
        assert abs(elapsed_time - expected_delay) < 2, f"Время {
            elapsed_time:.2f} не близко к {expected_delay} сек"
