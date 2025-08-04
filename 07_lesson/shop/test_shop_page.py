from selenium import webdriver
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from main_page_shop import MainPage
from inventory_page import InventoryPage
from shop_cart_page import CartPage
from checkout_step_one import ChecoutOnePage
from checkout_step_two import ChecoutTwoPage


@pytest.fixture()
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_shop(driver):
    #  вход на сайт
    main_page = MainPage(driver)

    # авторизуемся
    main_page.authorization('standard_user', 'secret_sauce')

    # нажимаем на login
    main_page.login_button()

    # добавляем товары в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")

    # нажимаем на checkout
    cart_page = CartPage(driver)
    cart_page.checkout_button()

    # заполняем форму
    one_step = ChecoutOnePage(driver)
    one_step.input_form("Zlata", "Sovik", 169933)

    # нажимаем на continue
    one_step.continue_button()

    # проводим проверку
    two_page = ChecoutTwoPage(driver)
    result = two_page.result_total()
    expected_result = "Total: $58.29"
    assert result == expected_result
