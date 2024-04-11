from base.base_class import BasePageClass
from base.locators_class import CatalogPageLocator


# url тестируемой страницы
catalog_url = 'https://www.vsemayki.ru/catalog'


class CatalogPage(BasePageClass, CatalogPageLocator):
    """Класс страницы каталога сайта"""

    def __init__(self, driver):
        super().__init__(driver)

    """Methods"""
    def enter_page(self):
        """method перехода на тестируемую страницу"""
        self.driver.get(catalog_url)
        self.driver.maximize_window()

    @staticmethod
    def method_expecting_same_values(first_value, second_value):
        """method сравнения резултатов одинаковых значений"""
        assert first_value == second_value

    @staticmethod
    def method_expecting_different_values(first_value, second_value):
        """method сравнения резултатов различных значений"""
        assert first_value != second_value
