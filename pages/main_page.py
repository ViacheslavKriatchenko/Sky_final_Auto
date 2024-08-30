from config.config_page import ConfigPage
from config.links import Links


class MainPage(ConfigPage):

    PAGE_URL = Links.HOST

    locators = [
        {'ENTER_BUTTON_LOCATOR': '//button[text()="Войти"]'}
    ]

    def click_login_button(self):
        self.driver.find_element('xpath', '//button[text()="Войти"]').click()
