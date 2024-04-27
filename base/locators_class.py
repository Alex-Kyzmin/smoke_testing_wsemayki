from dataclasses import dataclass


@dataclass
class GeneralPageLocator:
    """Датакласс локаторов главной страницы"""

    # локатор кнопки подтверждения местоположения
    loc_btn_alert_locality: str = '//button[@data-autotest="component-6"]'
    # локатор кнопки подтверждения принятия файлов cookie
    loc_btn_accept_cookie: str = '//button[@data-autotest="component-21"]'
    # локатор кнопки подтверждения информации о принтах
    loc_btn_accept_info: str = '//button[@class="_1bJ1Ky_4"]'

    # локатор ссылки "Корпоративным клиентам"
    loc_link_corporate_client: str = '//a[@href="https://opt.vsemayki.ru/"]'
    # локатор ссылки "Блогерам"
    loc_link_bloggers: str = '//a[@href="https://bloggers.vsemayki.ru/"]'
    # локатор ссылки "Вебмастерам"
    loc_link_webmasters: str = '//a[@href="https://webmasters.vsemayki.ru/"]'
    # локатор ссылки "Дизайнерам"
    loc_link_designers: str = '//a[@href="/landing/designer"]'
    # локатор ссылки "О нас"
    loc_link_about: str = '//a[@href="/doc/about"]'

    # локатор подсчета количества товара в "избранном" и "корзине для покупок"
    loc_amount_product: str = '//span[@class="H9B0OzDq"]'


@dataclass
class CatalogPageLocator(GeneralPageLocator):
    """Датакласс локаторов страницы каталога"""

    # локатор изображения товара
    loc_img: str = '//img[@class="img-fluid _90Cp5Gp7"]'
    # локатор изображения товара после наведения мыши
    loc_img_after_action: str = '//img[@class="img-fluid showback _3A-DxGKu"]'
    # локатор названия товара
    loc_name_product: str = '//span[@class="_38-vDi9W card__title"]'

    # локатор быстрого просмотра карточки товара
    loc_quick_view: str = '//div[text() = "Быстрый просмотр"]'
    # локатор кнопки закрытия формы быстрого просмотра товара
    loc_btn_close_quick_view: str = '//div[@class="_8tOwcCtC"]'

    # локаторы фильтра размера иконок товара
    loc_big_size_filter: str = '//div[@class="Yw3OIV4m _2jiPDrqc"]'
    loc_small_size_filter: str = '//div[@class="Yw3OIV4m _38D5WGC_"]'

    # локаторы фильтра новинки/популярное
    loc_filter: str = '//div[@data-autotest="Select-3"]'
    loc_filter_change: str = '//div[@class="select-option--2fQbU"]'

    # локаторы пагинации следующая/предидущая
    loc_next_page: str = '(//i[@class="icon--2FMZ1"])[6]'
    loc_previous_page: str = '(//i[@class="icon--2FMZ1"])[5]'


@dataclass
class ManWearPageLocator(CatalogPageLocator):
    """Датакласс локаторов мужских товаров"""

    # общий локатор товаров на странице
    loc_generic_product: str = '(//div[@class="_3vYFslUB"])[$]'

    # локатор кнопки добавить в избранное в карточке товара
    loc_btn_add_favorite: str = '//div[@class="_3pSlocOO"]'
    # локатор артикула в карточке товара
    loc_article_product: str = '//span[@class="_2NM0iNH6"]'
    # локатор кнопки добавлено в избранное в разделе избранное
    loc_btn_added_favorite: str = '//button[@class="_3inGxmJa _1tF2GquN _2kHaSAke"]'

    # локатор изображения в карточке товара
    loc_img_product_in_cart: str = '//div[@class="_3vYFslUB"]'
    # локатор кнопки добавлено в избранное в карточке товара
    loc_btn_added_favorite_in_cart: str = '//div[@class="_3pSlocOO _3bhbhGhQ"]'

    # локатор артикула в форме товара
    loc_article_in_form: str = '//span[@class="TzZcdK5N"]'
    # локатор цены со скидками в форме товара
    loc_price_in_form: str = '(//span[@class="price--1I8Le"])[1]'
    # локатор размера товара в форме товара
    loc_size_in_form: str = '(//a[@class="_16WXU0VI"])[1]'

    # локатор добавить товар в корзину
    loc_btn_add_in_cart: str = '//*[text() = "Добавить в корзину"]'

    # локатор артикула товара в корзине
    loc_article_in_cart: str = '//div[@class="MJBRg4up"]'
    # локатор кнопки удалить в корзине
    loc_btn_delete_in_cart: str = '//span[text()="Удалить товар"]'
    # локатор суммы заказа в корзине
    loc_general_price_in_cart: str = '(//span[@class="price--1JTB7"])[1]'
    # локатор оповещения "корзина пуста"
    loc_empty_in_cart: str = '//p[@class="_3-XmRGcC"]'
