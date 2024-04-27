import os

from datetime import datetime
from dotenv import load_dotenv
from environs import Env

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilites.logger import Logger as Log


load_dotenv()
env = Env()


class BasePageClass:
    """Базовый класс для страниц тестируемого сервиса"""

    def __init__(self, driver):
        """Инициализатор класса"""
        self.driver = driver

    """Getters"""
    def get_element_page(self, locator):
        """Getter обозначения элемента страницы"""
        return WebDriverWait(
            self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, locator)))

    """Actions"""
    def action_move_to_element(self, locator):
        """action - по наведению мыши на локатор"""
        action = ActionChains(self.driver)
        return action.move_to_element(self.get_element_page(locator=locator))

    """Methods"""
    def enter_page(self, name_url):
        """method перехода на тестируемую страницу"""
        Log.add_start_step('enter page')
        self.driver.get(name_url)
        self.driver.maximize_window()
        Log.add_end_step(url=f'{name_url}', method='enter page')
        print('Запрос на переход на страницу получен')

    def method_assert_url(self, name_url):
        """Method подтверждения перехода на заданную веб-страницу"""
        assert self.driver.current_url == name_url
        print('Подтверждение фактического url с ожидаемым')

    def method_make_screen(self, name_page: str):
        """Method получения текущего снимка экрана"""
        current_time = datetime.utcnow().strftime('%Y, %m, %d, %H, %M, %S')
        screenshot_name = 'screen ' + name_page + ' ' + current_time + '.png'
        self.driver.save_screenshot(os.getenv('path_screen') + screenshot_name)
        print('Сделан подтверждающий снимок экрана')
