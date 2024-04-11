from dataclasses import dataclass


@dataclass
class HomePageLocator:
    """Датакласс локаторов главной страницы"""

    # локатор кнопки подтверждения местоположения
    btn_alert_loc: str = '//button[@data-autotest="component-6"]'
    # локатор кнопки подтверждения файлов cookie
    btn_accept_cookie: str = '//button[@data-autotest="component-21"]'

    # локатор ссылки "Корпоративным клиентам"
    link_corporate_client_loc: str = '//*[@id="__next"]/div/header/div/div[1]/div[2]/div/div[1]/div'
    # локатор ссылки "Блогерам"
    link_bloggers_loc: str = '//*[@id="__next"]/div/header/div/div[1]/div[2]/div/div[2]/div'
    # локатор ссылки "Вебмастерам"
    link_webmasters_loc: str = '//*[@id="__next"]/div/header/div/div[1]/div[2]/div/div[3]/div'
    # локатор ссылки "Дизайнерам"
    link_designers_loc: str = '//*[@id="__next"]/div/header/div/div[1]/div[2]/div/div[4]/div'
    # локатор ссылки "О нас"
    link_about_loc: str = '//*[@id="__next"]/div/div[5]/div/div[1]/div[2]/div[2]/a[1]'


@dataclass
class CatalogPageLocator:
    """Датакласс локаторов страницы каталога"""

    # локатор кнопки подтверждения местоположения
    btn_alert_loc: str = '//button[@data-autotest="component-6"]'
    # локатор кнопки подтверждения файлов cookie
    btn_accept_cookie: str = '//button[@data-autotest="component-21"]'
    btn_accept_info_loc: str = '//button[@class="_1bJ1Ky_4"]'

    # локатор "мужской одежды"
    man_wear_loc: str = '//*[@id="manwear"]'

    # локатор изображения 1 товара
    first_product_image_loc: str = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/a/img[1]'
    # локатор названия 1 товара
    first_product_name_loc: str = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/div/span'

    # локатор фильтра маленьких значков товара
    small_paginate_filter_loc: str = '//div[@class="Yw3OIV4m _38D5WGC_"]'
    # локатор фильтра крупных значков товара
    big_paginate_filter_loc: str = '//div[@class="Yw3OIV4m _2jiPDrqc"]'
    # локатор фильтра новинок/популярные
    filter_loc: str = '//span[@data-autotest="Select"]'
    # локаторы фильтра новинок/популярные
    new_in_filter_loc: str = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]'
    pop_in_filter_loc: str = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]'
    # локаторы пагинации следующая/предидущая
    next_page_loc: str = '//a[@class="_33BvM8H- _2IwczoDq"]'
    previous_page_loc: str = '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[3]/div/a[1]'


@dataclass
class WearPageLocator:
    """Датакласс локаторов страниц каталогов продуктов"""

    # локатор кнопки подтверждения местоположения
    btn_alert_loc: str = '//button[@data-autotest="component-6"]'
    # локатор кнопки подтверждения файлов cookie
    btn_accept_cookie_loc: str = '//button[@data-autotest="component-21"]'
    # локатор кнопки подтверждения информации о "принтах"
    btn_accept_info_loc: str = '//button[@class="_1bJ1Ky_4"]'

    # локатор ссылки "избранное"
    link_favorite_loc: str = '//a[@href="/favorites"]'
    # локатор подсчета товаров в "избранном"
    span_amount_favorite_loc: str = '//span[@class="H9B0OzDq"]'
    # локаторы названий добавленных товаров в избранное
    first_added_prod_loc: str = '//*[@id="content"]/div/div/div[2]/div/div/div[1]/div/a/div/span'
    second_added_prod_loc: str = '//*[@id="content"]/div/div/div[2]/div/div/div[2]/div/a/div/span'
    # локатор добавленного товаров в избранное
    added_btn_loc: str = '//*[@id="content"]/div/div/div[2]/div/div/div[1]/div/button'

    # локаторы атрибутов товара в карточке товара
    vendor_code_cart_loc: str = '//*[@id="content"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/span'
    price_product_cart_loc: str = '//*[@id="content"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/span'
    size_product_cart_loc: str = '//*[@id="content"]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/a[2]'
    color_product_cart_loc: str = '//*[@id="content"]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/li/span'
    btn_add_basket_loc: str = '//*[@id="content"]/div[1]/div[2]/div[2]/div/div[2]/div[1]'

    size_loc_alert = '/html/body/div[5]/div/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div/i/svg'
    # локатор ссылки "корзины"
    link_basket_loc: str = '//*[@id="__next"]/div/header/div/div[2]/div[5]/div[3]/a'
    # локатор подсчета товаров в "корзины"
    span_amount_basket_loc: str = '//*[@id="__next"]/div/header/div/div[2]/div[5]/div[3]/a/div/span'

    # локаторы атрибутов 1 товара в корзине
    vendor_code_1_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[1]/div[3]/div[2]'
    price_1_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[1]/div[5]/div[1]/div/div[1]/span/span'
    size_1_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[1]/div[3]/div[4]/div[1]/div/div[1]/div/span/div/div'
    color_1_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[1]/div[3]/div[4]/div[1]/div/div[2]/div/span/div/div/span'

    # локаторы атрибутов 1 товара в корзине
    vendor_code_2_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[2]/div[3]/div[2]'
    price_2_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[2]/div[5]/div[1]/div/div[1]/span/span'
    size_2_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[2]/div[3]/div[4]/div[1]/div/div[1]/div/span/div/div'
    color_2_cart_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[2]/div[3]/div[4]/div[1]/div/div[2]/div/span/div/div/span'

    # локатор удаления 3 товара из корзины
    remove_3_product_loc: str = '//*[@id="content"]/div/div[1]/section/div[1]/div[3]/section[3]/div[3]/div[4]/div[2]/div[2]/span'

    # локатор суммы заказа
    order_price_loc: str = '//*[@id="content"]/div/div[1]/section/div[2]/div[2]/div[1]/div[2]/span/span'
