import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


"""Настройка драйвера управления Chrome"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# доп настройка в браузере Crome (позволяет работать со страницей без загрузки на 100%)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


@pytest.mark.run(order=1)
def test_enter_home_page(set_up):
    """Тестирование доступности главной страницы"""
    hp = HomePage(driver)
    # заходим на главную страницу
    hp.enter_site()
    # проверяем что находимся на необходимой url
    hp.method_assert_url(name_url='https://www.vsemayki.ru/')
    # делаем подтверждающий снимок экрана
    time.sleep(2)
    hp.method_make_screen(name_page='home_page')
    # подтверждаем свое местоположение
    hp.get_element_page(locator=hp.btn_alert_loc).click()
    print('Тест на переход на главную страницу пройден успешно!')


@pytest.mark.run(order=2)
def test_link():
    """Тестирование ссылок главной страницы"""

    def test_link_corporate_client():
        """Тестирование ссылки - Корпоративным клиентам"""
        hp = HomePage(driver)
        hp.enter_site()
        # переход по ссылке "Корпоративным клиентам"
        hp.get_element_page(locator=hp.link_corporate_client_loc).click()
        # переход на новую вкладку по ссылке "Корпоративным клиентам"
        driver.switch_to.window(driver.window_handles[1])
        # проверяем что находимся на необходимой url
        hp.method_assert_url(name_url='https://opt.vsemayki.ru/')
        # делаем подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='corporate_page')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print('Тест на переход по ссылке "Корпоративным клиентам" пройден успешно!')

    def test_link_bloggers():
        """Тестирование ссылки - Блогерам"""
        hp = HomePage(driver)
        hp.enter_site()
        # переход по ссылке "Блогерам"
        hp.get_element_page(locator=hp.link_bloggers_loc).click()
        # проверяем что находимся на необходимой url
        hp.method_assert_url(name_url='https://bloggers.vsemayki.ru/')
        # делаем подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='bloggers_page')
        print('Тест на переход по ссылке "Блогерам" пройден успешно!')

    def test_link_webmasters():
        """Тестирование ссылки - Вебмастерам"""
        hp = HomePage(driver)
        hp.enter_site()
        # переход по ссылке "Вебмастерам"
        hp.get_element_page(locator=hp.link_webmasters_loc).click()
        # проверяем что находимся на необходимой url
        hp.method_assert_url(name_url='https://webmasters.vsemayki.ru/')
        # делаем подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='webmasters_page')
        print('Тест на переход по ссылке "Вебмастерам" пройден успешно!')

    def test_link_designers():
        """Тестирование ссылки - Дизайнерам"""
        # заходим на главную страницу
        hp = HomePage(driver)
        hp.enter_site()
        # переход по ссылке "Дизайнерам"
        hp.get_element_page(locator=hp.link_designers_loc).click()
        # переход на новую вкладку по ссылке "Дизайнерам"
        driver.switch_to.window(driver.window_handles[1])
        # проверяем что находимся на необходимой url
        hp.method_assert_url(name_url='https://designers.vsemayki.ru/')
        # делаем подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='designers_page')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print('Тест на переход по ссылке "Дизайнерам" пройден успешно!')

    def test_link_about():
        """Тестирование ссылки - 'О нас' """
        hp = HomePage(driver)
        hp.enter_site()
        # переход по ссылке "О нас"
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        hp.get_element_page(locator=hp.link_about_loc).click()
        # проверяем что находимся на необходимой url
        hp.method_assert_url(name_url='https://www.vsemayki.ru/doc/about')
        # делаем подтверждающий снимок экрана
        time.sleep(2)
        hp.method_make_screen(name_page='about_page')
        print('Тест на переход по ссылке "О нас" пройден успешно!')

    def run_group_tests():
        """Функция запуска групы тестов"""
        test_link_corporate_client()
        test_link_bloggers()
        test_link_webmasters()
        test_link_designers()
        test_link_about()

    run_group_tests()
    driver.close()
