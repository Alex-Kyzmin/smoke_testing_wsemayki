import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.manwear_page import ManWearPage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# адреса тестируемых страниц
manwear_url = 'https://www.vsemayki.ru/catalog/view/manwear'
man_t_shirts_url = 'https://www.vsemayki.ru/catalog/group/man_tshirts'
man_sweatshirts_url = 'https://www.vsemayki.ru/catalog/group/mens_sweatshirts'
man_outerwear_url = 'https://www.vsemayki.ru/catalog/group/man_outerwear'
favorite_url = 'https://www.vsemayki.ru/favorites'
cart_url = 'https://www.vsemayki.ru/cart'


@pytest.mark.run(order=8)
def test_enter_manwears_page(set_up):
    """Тестирование доступности страниц тестируемых url"""
    list_testing_url = [
        man_t_shirts_url,
        man_sweatshirts_url,
        man_outerwear_url,
        favorite_url,
        cart_url
    ]
    mp = ManWearPage(driver)
    mp.enter_page(name_url=manwear_url)
    mp.action_accept_alerts()
    for url in list_testing_url:
        mp.enter_page(name_url=url)
        # проверка нахождения на необходимой url
        mp.method_assert_url(name_url=url)


@pytest.mark.run(order=9)
def test_add_favorites():
    """Тестирование возможности добавления товара в избранное"""
    selected_product = []
    mp = ManWearPage(driver)
    mp.enter_page(name_url=man_t_shirts_url)
    mp.method_add_in_favorite(selected_product)
    assert len(selected_product) == mp.get_amount_added()
    mp.enter_page(name_url=favorite_url)
    mp.get_element_page(locator=mp.loc_img_product_in_cart).click()
    article_product_favorite = mp.get_element_page(locator=mp.loc_article_product).text
    assert article_product_favorite in selected_product


@pytest.mark.run(order=10)
def test_quick_delete_favorites():
    """Тестирование возможности быстрого удаления товара из избранного"""
    mp = ManWearPage(driver)
    mp.enter_page(name_url=favorite_url)
    mp.method_quick_delete_in_favorite()


@pytest.mark.run(order=11)
def test_delete_favorites():
    """Тестирование возможности удаления товара из избранного"""
    selected_product = []
    driver.refresh()
    mp = ManWearPage(driver)
    mp.enter_page(name_url=man_outerwear_url)
    mp.method_add_in_favorite(selected_product)
    mp.enter_page(name_url=favorite_url)
    mp.get_element_page(locator=mp.loc_img_product_in_cart).click()
    mp.method_delete_in_favorite(selected_product)
    assert len(selected_product) == 0


@pytest.mark.run(order=12)
def test_quick_add_cart():
    """Тестирование возможности быстрого добавления товара в корзину"""
    selected_product = []
    mp = ManWearPage(driver)
    mp.enter_page(name_url=man_outerwear_url)
    mp.method_quick_add_in_cart(selected_product)
    assert len(selected_product) == mp.get_amount_added()
    mp.enter_page(name_url=cart_url)
    value_article_in_cart = mp.get_element_page(locator=mp.loc_article_in_cart).text
    article_in_cart = value_article_in_cart.replace('Арт.', 'Артикул:')
    assert article_in_cart in selected_product


@pytest.mark.run(order=13)
def test_delete_cart():
    """Тестирование возможности быстрого добавления товара в корзину"""
    mp = ManWearPage(driver)
    mp.enter_page(name_url=cart_url)
    mp.method_delete_in_cart()
    warning_information = mp.get_element_page(locator=mp.loc_empty_in_cart).text
    assert warning_information == 'В Вашей корзине пока нет товаров'


@pytest.mark.run(order=14)
def test_sum_calculation_logic():
    """Тестирование логики подсчета суммы заказа"""
    selected_product = []
    mp = ManWearPage(driver)
    mp.enter_page(name_url=man_sweatshirts_url)
    mp.method_add_in_cart(selected_product)
    mp.enter_page(name_url=man_outerwear_url)
    mp.method_add_in_cart(selected_product)
    time.sleep(3)
    assert len(selected_product) == mp.get_amount_added()
    mp.enter_page(name_url=cart_url)
    mp.method_sum_calculation_logic(selected_product)
    driver.close()
