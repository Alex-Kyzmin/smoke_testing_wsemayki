import random
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.wear_page import WearPage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# доп настройка в браузере Crome (позволяет работать со страницей без загрузки на 100%)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


@pytest.mark.run(order=5)
def test_favorites(set_up):
    """Тестирование возможности добавления/удаления товара в избранное"""

    # список названий товаров в избранном
    product_in_favorites = []

    # url тестируемых страниц
    man_wear_url = 'https://www.vsemayki.ru/catalog/view/manwear'
    bags_wear_url = 'https://www.vsemayki.ru/catalog/view/bags_and_backpacks'
    favorites_url = 'https://www.vsemayki.ru/favorites'

    wp = WearPage(driver)
    wp.method_enter_wear_page(url=man_wear_url)
    # проверка находиждения браузера на необходимой url
    wp.method_assert_url(name_url=man_wear_url)
    # подтверждаем alerts
    wp.action_accept_alerts()

    # добавляем случайный товар в избранное
    wp.method_add_product_in_favorite(
        num_product=random.choice(range(1, 12)),
        arg=product_in_favorites
    )
    # проверяем отображение количества товаров в избранном
    assert len(product_in_favorites) == wp.getter_amount_favorites()

    # переходим в другой вид товаров
    wp.method_enter_wear_page(url=bags_wear_url)
    wp.method_assert_url(name_url=bags_wear_url)
    # добавляем случайный товар в избранное
    wp.method_add_product_in_favorite(
        num_product=random.choice(range(1, 12)),
        arg=product_in_favorites
    )
    time.sleep(2)
    # проверяем отображение количества товаров в избранном
    assert len(product_in_favorites) == wp.getter_amount_favorites()

    # проверяем соответсвие выбранных товаров с фактическим содержанием "избранного"
    wp.action_click_link_favorites()
    time.sleep(2)
    wp.method_assert_url(name_url=favorites_url)
    time.sleep(5)
    # проверяем подтверждающий снимок экрана
    wp.method_make_screen(name_page='favorites')
    # получаем названия добавленных товаров
    first_product = wp.get_element_page(locator=wp.first_added_prod_loc).text
    second_product = wp.get_element_page(locator=wp.second_added_prod_loc).text
    # сравниваем их с товарами до помещение в избранное
    assert (product_in_favorites[0] == first_product
            and product_in_favorites[1] == second_product)
    print('Товары добавляются в "избранное" и соответсвуют выбранным!')

    # проверяем возможность удаления
    wp.method_remove_product_in_favorite(
        loc=wp.added_btn_loc,
        arg=product_in_favorites
    )
    assert len(product_in_favorites) == 1
    wp.method_remove_product_in_favorite(loc=wp.added_btn_loc, arg=product_in_favorites)
    assert len(product_in_favorites) == 0
    print('Товары удаляются из "избранного" и соответсвуют выбранным!')


@pytest.mark.run(order=6)
def test_basket():
    """Тестирование возможности добавления/удаления товара в корзине"""
    list_choice_products = []

    man_wear_url = 'https://www.vsemayki.ru/catalog/view/manwear'
    basket_url = 'https://www.vsemayki.ru/cart'

    wp = WearPage(driver)
    wp.method_enter_wear_page(url=man_wear_url)

    # Добавляем в корзину 3 случайных товара
    wp.method_add_product_in_cart(num_product=random.choice(range(1, 3)), args=list_choice_products)
    wp.method_enter_wear_page(url=man_wear_url)
    wp.method_add_product_in_cart(num_product=random.choice(range(4, 6)), args=list_choice_products)
    wp.method_enter_wear_page(url=man_wear_url)
    wp.method_add_product_in_cart(num_product=random.choice(range(7, 9)), args=list_choice_products)
    wp.method_enter_wear_page(url=man_wear_url)

    # Проверяем количество добавленных товаров
    assert len(list_choice_products) == wp.getter_amount_basket()
    print('Товары добавляются в корзину и их количество соответсвует ожидаемому!')

    # Переходим по ссылке в корзину покупок
    wp.action_click_link_basket()
    time.sleep(2)
    wp.method_assert_url(name_url=basket_url)
    # Делаем подтверждающий снимок экрана
    wp.method_make_screen(name_page='basket_page')

    # Проверяем возможность удаления 1-го из товаров
    wp.get_element_page(locator=wp.remove_3_product_loc).click()
    list_choice_products.pop()
    time.sleep(2)
    assert len(list_choice_products) == wp.getter_amount_basket()
    print('Возможность удалять товар из корзины проверена!')

    # Проверяем атрибуты добавленных товаров с товарами находящимися в корзине
    price_product_in_cart = []

    list_1_product = list_choice_products[0]
    vendor_code_1_product = list_1_product[0].replace('Артикул: ', '')
    price_1_product = int(list_1_product[1].replace(' ₽', '').replace(' ', ''))
    vendor_code_1_product_in_cart = (wp.get_element_page(
        locator=wp.vendor_code_1_cart_loc).text.replace('Арт. ', ''))
    price_1_product_in_cart = int(wp.get_element_page(
        locator=wp.price_1_cart_loc).text.replace(' ₽', '').replace(' ', ''))
    assert (vendor_code_1_product == vendor_code_1_product_in_cart
            and price_1_product == price_1_product_in_cart)
    price_product_in_cart.append(price_1_product)

    list_2_product = list_choice_products[1]
    vendor_code_2_product = list_2_product[0].replace('Артикул: ', '')
    price_2_product = int(list_2_product[1].replace(' ₽', '').replace(' ', ''))
    vendor_code_2_product_in_cart = (wp.get_element_page(
        locator=wp.vendor_code_2_cart_loc).text.replace('Арт. ', ''))
    price_2_product_in_cart = int(wp.get_element_page(
        locator=wp.price_2_cart_loc).text.replace(' ₽', '').replace(' ', ''))
    assert (vendor_code_2_product == vendor_code_2_product_in_cart
            and price_2_product == price_2_product_in_cart)
    price_product_in_cart.append(price_2_product)

    # Проверяем логику подсчета суммы заказа
    order_price = int(wp.get_element_page(
        locator=wp.order_price_loc).text.replace(' ₽', '').replace(' ', ''))
    sum_price_product = sum(price_product_in_cart)
    assert order_price == sum_price_product
    print('Логика подсчета суммы верна!')

    # Переход к оформлению заказа
    order_url = 'https://www.vsemayki.ru/cart/delivery'
    driver.get(order_url)
    time.sleep(2)
    wp.method_assert_url(name_url=order_url)
    wp.method_make_screen(name_page='order_page')
    driver.close()
