import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.catalog_page import CatalogPage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install())
)

# url тестируемой страницы
catalog_url = 'https://www.vsemayki.ru/catalog'


@pytest.mark.run(order=3)
def test_enter_catalog_page(set_up):
    """Тестирование доступности страницы каталога товаров"""
    cp = CatalogPage(driver)
    # переход на страницу каталога
    cp.enter_page(name_url=catalog_url)
    # подтверждение alerts
    cp.action_accept_alerts()
    # проверка нахождения на необходимой url
    cp.method_assert_url(name_url=catalog_url)
    # подтверждающий снимок экрана
    time.sleep(2)
    cp.method_make_screen(name_page='catalog_page')


@pytest.mark.run(order=4)
def test_change_image_for_act():
    """Тестирование изменения картинки при наведении мыши"""
    cp = CatalogPage(driver)
    cp.enter_page(name_url=catalog_url)
    # вызов тестового метода
    cp.method_check_change_image()


@pytest.mark.run(order=5)
def test_filters():
    """Тестирование фильтров товаров"""

    def test_sort_size_filter():
        """Тестирование фильтра больших/малых иконок товаров"""
        cp = CatalogPage(driver)
        cp.enter_page(name_url=catalog_url)
        # вызов тестового метода
        cp.method_sort_size_filter()

    def test_sort_filter():
        """Тестирование фильтра новинки/популярное"""
        cp = CatalogPage(driver)
        cp.enter_page(name_url=catalog_url)
        # вызов тестового метода
        cp.method_sort_filter()

    def run_group_tests():
        test_sort_size_filter()
        test_sort_filter()

    run_group_tests()


@pytest.mark.run(order=6)
def test_quick_view_form():
    """Тестирование открытия формы быстрого просмотра карты товара"""
    cp = CatalogPage(driver)
    cp.enter_page(name_url=catalog_url)
    # вызов тестового метода
    cp.method_quick_view_form()


@pytest.mark.run(order=7)
def test_pagination_page():
    """Тестирование пагинации страницы"""
    cp = CatalogPage(driver)
    cp.enter_page(name_url=catalog_url)
    # вызов тестового метода
    cp.method_pagination_page()
    driver.close()
