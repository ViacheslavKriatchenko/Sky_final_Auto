from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ConfigPage:

    def __init__(self, driver) -> None:
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.__driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'{self.PAGE_URL} is opened'):
            self.__wait.until(EC.url_to_be((self.PAGE_URL)))
