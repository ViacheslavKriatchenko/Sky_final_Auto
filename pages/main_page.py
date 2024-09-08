from config.config_page import ConfigPage
from selenium.webdriver.support import expected_conditions as EC
from config.ConfigProvider import ConfigProvider
from time import sleep
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(ConfigPage):

    # переопределение адреса страницы
    PAGE_URL = ConfigProvider().get(section='ui', prop='HOST')

    # page locators:
    ENTER_BUTTON_LOCATOR = ('xpath', '//button[text()="Войти"]')
    SEARCH_FIELD_LOCATOR = ('xpath', '//input[@name="kp_query"]')
    # menu
    ONLINE_KINOTEATR_LOCATOR = ('path', '//ul/li[2]/a')
    # search info
    SEARCH_MOVIE_INFO = ('xpath', '(//div[@class="element most_wanted"]//span)[2]')
    CALENDAR_SECTION = ('xpath', '//span[text()="Кассовые сборы за уик-энд"]')
    RELEASE_MOVIE = ('xpath', '//div[@class="styles_boxesWrapper__Q_srn"]/div[1]//li[2]/div//a')
    BUTTON_BUY = ('xpath', '//a[text()="Купить билеты"]')
    FIND_MOVIE = ('xpath', '//span[@class="film-header__content"]//a')

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
        result = self.wait.until(
            EC.visibility_of_element_located((self.SEARCH_MOVIE_INFO)), message="Объект не найден"
            )
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

    def movie_selection(self):
        with allure.step('Используем функцию actions'):
            action = ActionChains(self.driver)
        field = self.driver.find_element(*self.CALENDAR_SECTION)
        with allure.step('Делаем скролл к секции фильмов и элементу'):
            action.scroll_to_element(field).perform()
            self.driver.execute_script("""
            window.scrollTo({
                top: window.scrollY + 500,
            });
            """)
        take_movie = self.driver.find_element(*self.RELEASE_MOVIE)
        text_search = take_movie.text
        with allure.step('Переместить указатель и ждать окно'):
            action.move_to_element(take_movie).pause(3).perform()
        with allure.step('Нажать кнопку в появившимся окне'):
            self.wait.until(
                EC.element_to_be_clickable((self.BUTTON_BUY))
                ).click()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # для ручной отладки
        find_movie = self.driver.find_element(*self.FIND_MOVIE)
        text_find = find_movie.text
        return text_search, text_find

        # setTimeout(function(){debugger;}, 5000)
