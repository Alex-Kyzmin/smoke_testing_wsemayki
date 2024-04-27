import random

from base.base_class import BasePageClass
from base.locators_class import ManWearPageLocator
from utilites.logger import Logger as Log


class ManWearPage(BasePageClass, ManWearPageLocator):
    """Класс страницы мужского каталога"""

    """Getters"""
    @staticmethod
    def get_exact_locator(num, generic_locator):
        """Getter преобразования общего локатора в точный"""
        exact_locator = generic_locator.replace('$', str(num))
        return exact_locator

    def get_amount_added(self):
        """Getter подсчета добавленных товаров в иконках"""
        value_amount_added = self.get_element_page(locator=self.loc_amount_product).text
        return int(value_amount_added)

    """Actions"""
    def action_accept_alerts(self):
        """action - подтверждение alerts"""
        # подтверждение принятия файлов cookie
        self.get_element_page(locator=self.loc_btn_accept_cookie).click()
        # принятие информации о принтах
        self.get_element_page(locator=self.loc_btn_accept_info).click()
        # подтверждение меcтоположения
        self.get_element_page(locator=self.loc_btn_alert_locality).click()

    """Methods"""
    def method_add_in_favorite(self, selected_product: list):
        """method добавления случайного товара в избранное"""
        Log.add_start_step('method add in favorite')
        # получение случайного номера товара
        random_num_product = random.choice(range(1, 4))
        # преобразование общего локатора в точный
        loc_product = self.get_exact_locator(
            num=random_num_product,
            generic_locator=self.loc_generic_product
        )
        # нажатие на случайный товар
        self.get_element_page(locator=loc_product).click()
        # нажатие на кнопку добавить в избранное в карточке товара
        self.get_element_page(locator=self.loc_btn_add_favorite).click()
        # получение и запись артикула выбранного товара
        article_product = self.get_element_page(locator=self.loc_article_product).text
        selected_product.append(article_product)
        Log.add_end_step(url=f'{self.driver.current_url}', method='method add in favorite')
        print('случайный товар добавлен в избранное')
        # возврат атрибута выбранного товара для дальнейшего сравнения
        return selected_product

    def method_quick_delete_in_favorite(self):
        """method быстрого удаления товара из избранное"""
        Log.add_start_step('method quick delete in favorite')
        # нажатие на кнопку удалить из избранного
        self.get_element_page(locator=self.loc_btn_added_favorite).click()
        Log.add_end_step(url=f'{self.driver.current_url}', method='method quick delete in favorite')
        print('добавленный товар удален из избранного')

    def method_delete_in_favorite(self, selected_product: list):
        """method удаления товара из избранное"""
        Log.add_start_step('method delete in favorite')
        # нажатие на кнопку удалить из избранного
        self.get_element_page(locator=self.loc_btn_added_favorite_in_cart).click()
        # изменение записей выбранных товаров после удаления
        selected_product.pop()
        Log.add_end_step(url=f'{self.driver.current_url}', method='method delete in favorite')
        print('добавленный товар удален из избранного')
        # возврат записей выбранных товаров для дальнейшего сравнения
        return selected_product

    def method_quick_add_in_cart(self, selected_product: list):
        """method быстрого добавления товара в корзину"""
        Log.add_start_step('method quick add in cart')
        # наведение мыши на изображения товара, для открытия скрытого локатора
        self.action_move_to_element(locator=self.loc_img).perform()
        # клик по скрытой форме быстрого просмотра товара
        self.get_element_page(locator=self.loc_quick_view).click()
        # клик по кнопке "добавить в корзину" в форме быстрого просмотра товара
        self.get_element_page(locator=self.loc_btn_add_in_cart).click()
        # получение и запись артикула товара для дальнейшего сравнения
        article_product = self.get_element_page(locator=self.loc_article_in_form).text
        selected_product.append(article_product)
        Log.add_end_step(url=f'{self.driver.current_url}', method='method quick add in cart')
        print('товар добавлен в корзину')
        # возврат атрибута выбранного товара для дальнейшего сравнения
        return selected_product

    def method_add_in_cart(self, selected_product: list):
        """method добавления товара в корзину"""
        Log.add_start_step('method add in favorite')
        # получение случайного номера товара
        random_num_product = random.choice(range(1, 4))
        # приобразование общего локатора в точный
        loc_product = self.get_exact_locator(
            num=random_num_product,
            generic_locator=self.loc_generic_product
        )
        # добавление товара в корзину с параметрами
        self.get_element_page(locator=loc_product).click()
        self.get_element_page(locator=self.loc_size_in_form).click()
        self.get_element_page(locator=self.loc_btn_add_in_cart).click()
        # получение и запись атрибута цены товара для дальнейшего сравнения
        value_price_product = self.get_element_page(locator=self.loc_price_in_form).text
        price_product = int(value_price_product.replace(' ₽', '').replace(' ', ''))
        selected_product.append(price_product)
        Log.add_end_step(url=f'{self.driver.current_url}', method='method add in favorite')
        print('товар добавлен в корзину')
        # возврат атрибута выбранного товара для дальнейшего сравнения
        return selected_product

    def method_delete_in_cart(self):
        """method удаления товара из избранное"""
        Log.add_start_step('method delete in cart')
        # нажатие на кнопку удалить товар в корзине
        self.get_element_page(locator=self.loc_btn_delete_in_cart).click()
        Log.add_end_step(url=f'{self.driver.current_url}', method='method delete in cart')
        print('выбранный товар удален из корзины')

    def method_sum_calculation_logic(self, selected_product: list):
        """method подсчета суммы заказа"""
        Log.add_start_step('method sum calculation logic')
        # получение и запись атрибута суммы заказа в корзине для покупок
        value_general_price = self.get_element_page(locator=self.loc_general_price_in_cart).text
        general_price = int(value_general_price.replace(' ₽', '').replace(' ', ''))
        # сравнение результатов сыммы каждого товара с суммой заказа
        assert general_price == sum(selected_product)
        Log.add_end_step(url=f'{self.driver.current_url}', method='method sum calculation logic')
        print('Логика подсчета суммы заказа проверена')
