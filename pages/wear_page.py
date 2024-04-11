from selenium.webdriver import ActionChains

from base.base_class import BasePageClass
from base.locators_class import WearPageLocator


class WearPage(BasePageClass, WearPageLocator):
    """Класс страницы каталога сайта"""

    def __init__(self, driver):
        super().__init__(driver)

    # матрица локаторов товаров
    matrix_product_loc = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[$]'
    # матрица локатора кнопки быстро добавить товар в "избранное"
    matrix_btn_fast_add_favorite = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[$]/div/button'
    # матрица локатора названия товара
    matrix_name_product_loc = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[$]/div/a/div/span'
    # матрица локатора алерта быстрого просмотра товара
    matrix_btn_viewing_alert_loc = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[$]/div/div[1]/div/button'

    """Getters"""
    def getter_amount_favorites(self):
        """getter получения количества товаров в избранном"""
        return int(self.get_element_page(locator=self.span_amount_favorite_loc).text)

    def getter_amount_basket(self):
        """getter получения количества товаров в избранном"""
        return int(self.get_element_page(locator=self.span_amount_basket_loc).text)

    """Actions"""
    def action_move_to_element(self, locator):
        """action перемещения до объекта страницы"""
        action = ActionChains(self.driver)
        return action.move_to_element(self.get_element_page(locator))

    def action_click_link_favorites(self):
        """action перехода в избранное"""
        return self.get_element_page(locator=self.link_favorite_loc).click()

    def action_click_link_basket(self):
        """action перехода в карзину"""
        return self.get_element_page(locator=self.link_basket_loc).click()

    """Methods"""
    def method_enter_wear_page(self, url):
        """method перехода на тестируемую страницу"""
        self.driver.get(url)
        self.driver.maximize_window()

    def method_add_product_in_favorite(self, num_product, arg):
        """method добавления случайного товара в избранное"""
        product_loc = self.matrix_product_loc.replace('$', str(num_product))
        add_product_loc = self.matrix_btn_fast_add_favorite.replace('$', str(num_product))
        name_product_loc = self.matrix_name_product_loc.replace('$', str(num_product))
        self.action_move_to_element(product_loc).perform()
        self.get_element_page(add_product_loc).click()
        arg.append(self.get_element_page(name_product_loc).text)

    def method_remove_product_in_favorite(self, loc, arg):
        """method удаления товара из избранного"""
        self.get_element_page(locator=loc).click()
        arg.pop()

    def method_add_product_in_cart(self, num_product, args):
        """method добавления случайного товара в корзину"""
        list_product = []

        product_loc = self.matrix_name_product_loc.replace('$', str(num_product))
        self.action_move_to_element(locator=product_loc).click().perform()
        name_product = self.get_element_page(locator=self.vendor_code_cart_loc)
        list_product.append(name_product.text)
        price_product = self.get_element_page(locator=self.price_product_cart_loc)
        list_product.append(price_product.text)
        size_product = self.get_element_page(locator=self.size_product_cart_loc)
        size_product.click()
        list_product.append(size_product.text)
        color_product = self.get_element_page(locator=self.color_product_cart_loc)
        color_product.click()
        list_product.append(color_product.text)
        args.append(list_product)
        self.get_element_page(locator=self.btn_add_basket_loc).click()
