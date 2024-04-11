import time
import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.catalog_page import CatalogPage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# доп настройка в браузере Crome (позволяет работать со страницей без загрузки на 100%)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


@pytest.mark.run(order=3)
def test_enter_catalog_page(set_up):
    """Тестирование доступности страницы каталога товаров"""
    cp = CatalogPage(driver)
    # переход на страницу каталога
    cp.enter_page()
    # проверка находиждения браузера на необходимой url
    cp.method_assert_url(name_url='https://www.vsemayki.ru/catalog')
    # делаем подтверждающий снимок экрана
    time.sleep(2)
    cp.method_make_screen(name_page='catalog_page')
    print('Тест на переход на страницу каталога пройден успешно!')


@pytest.mark.run(order=4)
def test_inspection_product():
    """Тестирование осмотра товаров в каталогах"""

    def test_sort_size_filter():
        """Тестирование фильтра размера иконок товаров"""
        cp = CatalogPage(driver)
        cp.enter_page()
        # переход в каталог "мужской одежды"
        cp.get_element_page(locator=cp.man_wear_loc).click()
        cp.get_element_page(locator=cp.btn_alert_loc).click()
        cp.get_element_page(locator=cp.btn_accept_cookie_loc).click()
        cp.get_element_page(locator=cp.btn_accept_info_loc).click()
        # получаем атрибут изображения и название 1 товара до фильтрации
        # так как по логике фильтра последовательность товаров не должна меняться
        image_before_sort = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        name_before_sort = cp.get_element_page(locator=cp.first_product_name_loc).text
        # активируем фильтр большого размера товара
        cp.get_element_page(locator=cp.big_paginate_filter_loc).click()
        # получаем атрибут изображения и название 1 товара после фильтрации
        image_after_sort = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        name_after_sort = cp.get_element_page(locator=cp.first_product_name_loc).text
        # проверка на изменение изображения (по размеру) и без изменения названия товара
        cp.method_expecting_different_values(first_value=image_before_sort, second_value=image_after_sort)
        cp.method_expecting_same_values(first_value=name_before_sort, second_value=name_after_sort)
        # возврат на первоначальный фильтр и сверка с начальным резултатом по изображению
        cp.get_element_page(locator=cp.small_paginate_filter_loc).click()
        image_after_return_filter = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        # проверка на возвращение изображения после дефильтрования
        cp.method_expecting_same_values(first_value=image_before_sort, second_value=image_after_return_filter)
        print('Тест на фильтр по изменению размера для читаемости товара пройден!')

    def test_sort_new_filter():
        """Тестирование фильтра размера иконок товаров"""
        cp = CatalogPage(driver)
        cp.enter_page()
        cp.get_element_page(locator=cp.man_wear_loc).click()
        # получаем атрибут изображения и название 1 товара до фильтрации
        # так как по логике фильтра последовательность товаров на странице должна измениться
        image_before_sort = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        name_before_sort = cp.get_element_page(locator=cp.first_product_name_loc).text
        # активируем фильтр "новинки"
        cp.get_element_page(locator=cp.filter_loc).click()
        cp.get_element_page(locator=cp.new_in_filter_loc).click()
        # получаем атрибут изображения и название 1 товара после фильтрации
        image_after_sort = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        name_after_sort = cp.get_element_page(locator=cp.first_product_name_loc).text
        # проверка на изменение 1 товара в списке (по изображению и названию)
        cp.method_expecting_different_values(first_value=image_before_sort, second_value=image_after_sort)
        cp.method_expecting_different_values(first_value=name_before_sort, second_value=name_after_sort)
        cp.get_element_page(locator=cp.filter_loc).click()
        cp.get_element_page(locator=cp.pop_in_filter_loc).click()
        # получаем атрибуты 1 товара после возврата фильтра по умолчанию
        image_after_sort_default = cp.get_element_page(locator=cp.first_product_image_loc).get_attribute('src')
        name_after_sort_default = cp.get_element_page(locator=cp.first_product_name_loc).text
        # проверка на возвращение товара при назначение фильтра по умолчанию
        cp.method_expecting_same_values(first_value=image_before_sort, second_value=image_after_sort_default)
        cp.method_expecting_same_values(first_value=name_before_sort, second_value=name_after_sort_default)
        print('Тест фильтра новинки/популярное пройден!')

    def test_pagination_page():
        """Тестирование пагинации страницы"""
        cp = CatalogPage(driver)
        cp.enter_page()
        cp.get_element_page(locator=cp.man_wear_loc).click()
        # получаем название 1 товара до перехода по пагинации
        name_before_pagination = cp.get_element_page(locator=cp.first_product_name_loc).text
        action = ActionChains(driver)
        # принимаем файлы cookie
        action.move_to_element(cp.get_element_page(locator=cp.next_page_loc)).click().perform()
        # получаем название 1 товара после перехода по пагинации
        name_after_pagination = cp.get_element_page(locator=cp.first_product_name_loc).text
        cp.method_expecting_different_values(first_value=name_before_pagination, second_value=name_after_pagination)
        action.move_to_element(cp.get_element_page(locator=cp.previous_page_loc)).click().perform()
        name_return_pagination = cp.get_element_page(locator=cp.first_product_name_loc).text
        cp.method_expecting_same_values(first_value=name_before_pagination, second_value=name_return_pagination)
        print('Тест на пагинацию страницы каталога пройден!')

    def run_group_tests():
        """Функция запуска групы тестов"""
        test_sort_size_filter()
        test_sort_new_filter()
        test_pagination_page()

    run_group_tests()
    driver.close()
