from config.config_page import ConfigPage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from config.ConfigProvider import ConfigProvider


class MainPage(ConfigPage):

    #  PAGE_URL = Links.HOST
    PAGE_URL = ConfigProvider().get(section='ui', prop='HOST')  # что лучше

    # page locators:
    locators = [
        {'ENTER_BUTTON_LOCATOR': '//button[text()="Войти"]'}
    ]
    ENTER_BUTTON_LOCATOR = ('xpath', '//button[text()="Войти"]')
    SEARCH_FIELD_LOCATOR = ('xpath' '//input[@name="kp_query"]')

    # functions:
    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.ENTER_BUTTON_LOCATOR))
            ).click()

    def enter_search_data(self, data: str) -> str:
        input_data = self.wait.until(
            EC.element_to_be_clickable((self.SEARCH_FIELD_LOCATOR))
            ).send_keys(data)
        return input_data
