from base.base_class import BasePageClass
from base.locators_class import HomePageLocator


# url тестируемой страницы
home_url = 'https://www.vsemayki.ru/'


class HomePage(BasePageClass, HomePageLocator):
    """Класс главной страницы сайта"""

    def __init__(self, driver):
        super().__init__(driver)

    """Methods"""
    def enter_site(self):
        """method перехода на тестируемую страницу"""
        self.driver.get(home_url)
        self.driver.maximize_window()
