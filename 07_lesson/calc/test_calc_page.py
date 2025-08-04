from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from main_page_calc import MainPage


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calc(driver):

    # фиксируем to be
    expected_result = 15
    expected_delay = 45

    #  вход на сайт
    main_page = MainPage(driver)

    #  задаем значение таймера
    main_page.delay(45)

    # вводим арифметику
    main_page.button_calc('7')
    main_page.button_calc('+')
    main_page.button_calc('8')

    # фиксируем начало теста
    start_time = time.time()

    # запускаем решение арифметики
    main_page.button_calc("=")
    main_page.wait_delay(46, 15)

    # фиксируем окончание арифметики
    end_time = time.time()
    elapsed_time = end_time - start_time

    #  фиксируем результат арифметики
    as_is_num = main_page.result_calc()

    # производим проверку
    assert as_is_num == expected_result, f"Резултат {as_is_num} != {
        expected_result}"
    assert abs(elapsed_time - expected_delay) < 2, f"Время {
        elapsed_time:.2f} не близко к {expected_delay} сек"
