from config.config_page import ConfigPage
from selenium.webdriver.support import expected_conditions as EC
from config.ConfigProvider import ConfigProvider
from time import sleep
import allure
from selenium.webdriver.common.keys import Keys


class MainPage(ConfigPage):

    PAGE_URL = ConfigProvider().get(section='ui', prop='HOST')

    # page locators:
    ENTER_BUTTON_LOCATOR = ('xpath', '//button[text()="Войти"]')
    SEARCH_FIELD_LOCATOR = ('xpath', '//input[@name="kp_query"]')
    # menu
    ONLINE_KINOTEATR_LOCATOR = ('path', '//ul/li[2]/a')
    # search info
    SEARCH_MOVIE_INFO = ('xpath', '(//div[@class="element most_wanted"]//span)[2]')

    # functions:
    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.ENTER_BUTTON_LOCATOR)), message="Кнопка 'Войти' не найдена"
            ).click()

    @allure.step('Ввести в поле данные')
    def enter_search_data(self, data: str):
        field = self.wait.until(
            EC.element_to_be_clickable((self.SEARCH_FIELD_LOCATOR))
            )
        field.clear()
        field.send_keys(data)
        field.send_keys(Keys.ENTER)
        result = self.wait.until(EC.visibility_of_element_located((self.SEARCH_MOVIE_INFO)))
        return result.text

    def click_menu_button(self):
        buttons = self.driver.find_elements('xpath', '(//nav/ul/li/a)')
        for button in buttons[10:18]:
            href = button.get_attribute('href')
            button.click()
            sleep(5)
            page_url = self.driver.current_url
            sleep(5)
            assert href == page_url
            self.driver.back()
            self.wait.until(EC.element_to_be_clickable((button)))
