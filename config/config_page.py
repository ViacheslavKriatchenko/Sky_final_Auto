from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config.ConfigProvider import ConfigProvider


class ConfigPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver, timeout=ConfigProvider().getint(
                section='common', prop='time'
                ), poll_frequency=1
            )

    def open_the_page(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def page_is_opened(self):
        with allure.step(f'{self.PAGE_URL} is opened'):
            self.wait.until(EC.url_to_be((self.PAGE_URL)))

    @allure.step('Взять текущий URL')
    def get_current_url(self):
        URL = self.driver.current_url
        return URL

    @allure.step('Сделать скриншот и сохранить в корень проекта как error.png')
    def save_screenshot(self):
        self.driver.save_screenshot('error.png')
