from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePageClass:
    """Базовый класс для страниц тестируемого сервиса"""

    def __init__(self, driver):
        self.driver = driver

    # локатор кнопки подтверждения местоположения
    btn_alert_loc: str = '//button[@data-autotest="component-6"]'
    # локатор кнопки подтверждения файлов cookie
    btn_accept_cookie_loc: str = '//button[@data-autotest="component-21"]'
    # локатор кнопки подтверждения информации о "принтах"
    btn_accept_info_loc: str = '//button[@class="_1bJ1Ky_4"]'

    """Getters"""
    def get_element_page(self, locator):
        """Getter обозначения элемента страницы"""
        return WebDriverWait(
            self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, locator)))

    """Action"""
    def action_accept_alerts(self):
        """Action принимающий alerts"""
        self.get_element_page(locator=self.btn_alert_loc).click()
        self.get_element_page(locator=self.btn_accept_cookie_loc).click()
        self.get_element_page(locator=self.btn_accept_info_loc).click()

    """Methods"""
    def method_assert_url(self, name_url):
        """Method подтверждения перехода на заданную веб-страницу"""
        assert self.driver.current_url == name_url
        print('Подтверждение фактического url с ожидаемым')

    def method_make_screen(self, name_page: str):
        """Method получения текущего снимка экрана"""
        current_time = datetime.utcnow().strftime('%Y, %m, %d, %H, %M, %S')
        path_file = 'C:\\Users\\Александр\\PycharmProjects\\VseMaykiTestingSite\\screen\\'
        screenshot_name = 'screen ' + name_page + ' ' + current_time + '.png'
        self.driver.save_screenshot(path_file + screenshot_name)
