from config.config_page import ConfigPage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links
import allure


class OnlineCinemaPage(ConfigPage):

    PAGE_URL = Links.ONLINE_CINEMA_PAGE

    SUBSCRIBE_BUTTON_LOCATOR = (
        'xpath', '//button[@data-test-id="SubscriptionPurchaseButton"]'
        )
    FIRST_MOVIE_LOCATOR = ('xpath', '//div[@data-tid="SelectionList"]/section[2]//li[1]')
    BOOKMARK_LOCATOR = ('xpath', '//button[@name="Bookmark"]')

    def click_subscribe_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SUBSCRIBE_BUTTON_LOCATOR))
            ).click()

    @allure.step('Выбор первого фильма из раздела Смотрят сейчас')
    def click_movie(self):
        self.wait.until(
            EC.element_to_be_clickable((self.FIRST_MOVIE_LOCATOR))
            ).click()

    @allure.step('Нажатие на иконку "Добавить в закладки"')
    def click_bookmark(self):
        self.wait.until(
            EC.element_to_be_clickable((self.BOOKMARK_LOCATOR))
            ).click()
