from base.base_class import BasePageClass
from base.locators_class import GeneralPageLocator


class HomePage(BasePageClass, GeneralPageLocator):
    """Класс главной страницы сайта"""

    """Actions"""
    def action_click_link(self, locator):
        """action - клик по ссылке"""
        self.get_element_page(locator=locator).click()
