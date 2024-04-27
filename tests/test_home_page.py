import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# доп настройка (позволяет работать со страницей без загрузки на 100%)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install())
)

# url тестируемой страницы
home_url = 'https://www.vsemayki.ru/'


@pytest.mark.run(order=1)
def test_enter_home_page(set_up):
    """Тестирование доступности главной страницы"""
    hp = HomePage(driver)
    hp.enter_page(name_url=home_url)
    # проверка нахождения на необходимой url
    hp.method_assert_url(name_url=home_url)
    # подтверждающий снимок экрана
    time.sleep(2)
    hp.method_make_screen(name_page='home_page')


@pytest.mark.run(order=2)
def test_link():
    """Тестирование ссылок главной страницы"""

    def test_link_corporate_client():
        """Тестирование ссылки - Корпоративным клиентам"""
        hp = HomePage(driver)
        hp.enter_page(name_url=home_url)
        corporate_client_page = 'https://opt.vsemayki.ru/'
        # переход по ссылке "Корпоративным клиентам"
        hp.action_click_link(locator=hp.loc_link_corporate_client)
        # переход на новую вкладку браузера
        driver.switch_to.window(driver.window_handles[1])
        # проверка нахождения на необходимой url
        hp.method_assert_url(name_url=corporate_client_page)
        # подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='corporate_page')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_link_bloggers():
        """Тестирование ссылки - Блогерам"""
        hp = HomePage(driver)
        hp.enter_page(name_url=home_url)
        bloggers_page = 'https://bloggers.vsemayki.ru/'
        # переход по ссылке "Блогерам"
        hp.action_click_link(locator=hp.loc_link_bloggers)
        # проверка нахождения на необходимой url
        hp.method_assert_url(name_url=bloggers_page)
        # подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='bloggers_page')

    def test_link_webmasters():
        """Тестирование ссылки - Вебмастерам"""
        hp = HomePage(driver)
        hp.enter_page(name_url=home_url)
        webmasters_page = 'https://webmasters.vsemayki.ru/'
        # переход по ссылке "Вебмастерам"
        hp.action_click_link(locator=hp.loc_link_webmasters)
        # проверка нахождения на необходимой url
        hp.method_assert_url(name_url=webmasters_page)
        # подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='webmasters_page')

    def test_link_designers():
        """Тестирование ссылки - Дизайнерам"""
        hp = HomePage(driver)
        hp.enter_page(name_url=home_url)
        designers_page = 'https://designers.vsemayki.ru/'
        # переход по ссылке "Дизайнерам"
        hp.action_click_link(locator=hp.loc_link_designers)
        # переход на новую вкладку браузера
        driver.switch_to.window(driver.window_handles[1])
        # проверка нахождения на необходимой url
        hp.method_assert_url(name_url=designers_page)
        # подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='designers_page')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_link_about():
        """Тестирование ссылки - 'О нас' """
        hp = HomePage(driver)
        hp.enter_page(name_url=home_url)
        about_page = 'https://www.vsemayki.ru/doc/about'
        # переход по ссылке "О нас"
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        hp.action_click_link(locator=hp.loc_link_about)
        # проверка нахождения на необходимой url
        hp.method_assert_url(name_url=about_page)
        # подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='about_page')

    def run_group_tests():
        """Функция запуска групы тестов"""
        test_link_corporate_client()
        test_link_bloggers()
        test_link_webmasters()
        test_link_designers()
        test_link_about()

    run_group_tests()
    driver.close()
