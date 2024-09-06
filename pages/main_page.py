from config.config_page import ConfigPage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from config.ConfigProvider import ConfigProvider
from time import sleep
import allure


class MainPage(ConfigPage):

    #  PAGE_URL = Links.HOST
    PAGE_URL = ConfigProvider().get(section='ui', prop='HOST')  # что лучше

    # page locators:
    locators = [
        {'ENTER_BUTTON_LOCATOR': '//button[text()="Войти"]'}
    ]
    ENTER_BUTTON_LOCATOR = ('xpath', '//button[text()="Войти"]')
    SEARCH_FIELD_LOCATOR = ('xpath' '//input[@name="kp_query"]')
    # menu
    ONLINE_KINOTEATR_LOCATOR = ('path', '//ul/li[2]/a')

    # functions:
    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.ENTER_BUTTON_LOCATOR))
            ).click()

    @allure.step('Ввести в поле данные - {data}')
    def enter_search_data(self, data: str) -> str:
        input_data = self.wait.until(
            EC.element_to_be_clickable((self.SEARCH_FIELD_LOCATOR))
            ).send_keys(data)
        return input_data

    def click_menu_button(self):
        buttons = self.driver.find_elements('xpath', '(//nav/ul/li/a)')
        for button in buttons[10:18]:
            href = button.get_attribute('href')
            button.click()
            sleep(5)
            page_url = self.driver.current_url
            assert href == page_url
            self.driver.back()
            self.wait.until(EC.element_to_be_clickable((button)))
