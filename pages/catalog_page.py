import time

from base.base_class import BasePageClass
from base.locators_class import CatalogPageLocator
from utilites.logger import Logger as Log


class CatalogPage(BasePageClass, CatalogPageLocator):
    """Класс страницы каталога сайта"""

    """Actions"""
    def action_accept_alerts(self):
        """action - подтверждение alerts"""
        # подтверждение меcтоположения
        self.get_element_page(locator=self.loc_btn_alert_locality).click()
        # подтверждение принятия файлов cookie
        self.get_element_page(locator=self.loc_btn_accept_cookie).click()
        # принятие информации о принтах
        self.get_element_page(locator=self.loc_btn_accept_info).click()

    """Methods"""
    def method_check_change_image(self):
        """method - проверки изменения картинки товара при наведении мыши"""
        Log.add_start_step('method check change image')
        # получение изображения товара до наведения мыши
        image_before_action = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        # наведение мыши на изображение
        self.action_move_to_element(locator=self.loc_img).perform()
        time.sleep(2)
        # получение изображения товара после наведения мыши
        image_after_action = self.get_element_page(
            locator=self.loc_img_after_action).get_attribute('src')
        # сравнение результатов
        assert image_before_action != image_after_action
        Log.add_end_step(url=f'{self.driver.current_url}', method='method check change image')
        print('проверено изменение картинки товара при наведении мыши')

    def method_sort_size_filter(self):
        """method - проверки фильтра размера иконок товаров"""
        Log.add_start_step('method sort size filter')
        # получение атрибута изображения и название 1 товара до фильтрации
        # так как по логике фильтра последовательность товаров не должна меняться
        image_before_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_before_sort = self.get_element_page(locator=self.loc_name_product).text
        # активация фильтра большого размера товара
        self.get_element_page(locator=self.loc_big_size_filter).click()
        # получение атрибута изображения и название 1 товара после фильтрации
        image_after_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_after_sort = self.get_element_page(locator=self.loc_name_product).text
        # проверка на разность изображений и равность названий
        assert image_before_sort != image_after_sort and name_before_sort == name_after_sort
        # возврат размера иконок по умолчанию
        self.get_element_page(locator=self.loc_small_size_filter).click()
        # получение атрибута изображения и название 1 товара после возврата первоначального фильтра
        image_after_return_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_after_return_sort = self.get_element_page(locator=self.loc_name_product).text
        # проверка на равность атрибутов товара после возврата первоначального фильтра
        assert image_before_sort == image_after_return_sort and name_before_sort == name_after_return_sort
        Log.add_end_step(url=f'{self.driver.current_url}', method='method sort size filter')
        print('проверены фильтры разных размеров иконок товаров')

    def method_sort_filter(self):
        """method - проверки фильтра популярное/новинки"""
        Log.add_start_step('method sort new filter')
        # получение атрибута изображения и название 1 товара до фильтрации
        # так как по логике фильтра последовательность товаров должна измениться
        image_before_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_before_sort = self.get_element_page(locator=self.loc_name_product).text
        # активация фильтра популярное/новинки товара
        self.get_element_page(locator=self.loc_filter).click()
        self.get_element_page(locator=self.loc_filter_change).click()
        # получение атрибута изображения и название 1 товара после фильтрации
        time.sleep(2)
        image_after_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_after_sort = self.get_element_page(locator=self.loc_name_product).text
        # проверка на разность атрибутов товара
        assert image_before_sort != image_after_sort and name_before_sort != name_after_sort
        # возврат фильтра по умолчанию
        self.get_element_page(locator=self.loc_filter).click()
        self.get_element_page(locator=self.loc_filter_change).click()
        # получение атрибута изображения и название 1 товара после возврата первоначального фильтра
        time.sleep(2)
        image_after_return_sort = self.get_element_page(
            locator=self.loc_img).get_attribute('src')
        name_after_return_sort = self.get_element_page(locator=self.loc_name_product).text
        # проверка на равность атрибутов товара после возврата первоначального фильтра
        assert image_before_sort == image_after_return_sort and name_before_sort == name_after_return_sort
        # логирование метода
        Log.add_end_step(url=f'{self.driver.current_url}', method='method sort new filter')
        print('проверены фильтры популярное/новинки')

    def method_quick_view_form(self):
        """method - открытия/закрытия формы быстрого просмотра товара"""
        Log.add_start_step('method quick view form')
        # наведение мыши на товар для получения доступа к форме быстрого просмотра
        self.action_move_to_element(locator=self.loc_img).perform()
        # открываем форму быстрого просмотра товара
        self.get_element_page(locator=self.loc_quick_view).click()
        time.sleep(1)
        # подтверждающий снимок экрана
        self.method_make_screen(name_page='quick_view_product_form')
        # закрытие формы быстрого просмотра товара
        self.get_element_page(locator=self.loc_btn_close_quick_view).click()
        Log.add_end_step(url=f'{self.driver.current_url}', method='method quick view form')
        print('проверена форма быстрого просмотра товара')

    def method_pagination_page(self):
        """method пагинации страницы"""
        Log.add_start_step('method pagination page')
        # получение названия 1 товара сраницы до пагинации
        name_product_before_pag = self.get_element_page(locator=self.loc_name_product).text
        # нажатие на кнопку следующая страница
        self.action_move_to_element(locator=self.loc_next_page).click().perform()
        # получение названия 1 товара сраницы после пагинации
        name_product_after_pag = self.get_element_page(locator=self.loc_name_product).text
        # сравнение на различность названий 1 товара на странице
        assert name_product_before_pag != name_product_after_pag
        # нажатие на кнопку пердыдущая страница
        self.action_move_to_element(locator=self.loc_previous_page).click().perform()
        # получение названия 1 товара сраницы после возврата на страницу
        name_product_return_pag = self.get_element_page(locator=self.loc_name_product).text
        # сравнение на идентичность названий 1 товара после возврата на страницу
        assert name_product_before_pag == name_product_return_pag
        Log.add_end_step(url=f'{self.driver.current_url}', method='method pagination page')
        print('проверена пагинация страниц каталога')
