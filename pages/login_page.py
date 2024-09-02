from config.config_page import ConfigPage
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(ConfigPage):

    # page locators:
    INPUT_LOGIN_LOCATOR = ('xpath', '//input[@name="login"]')
    BUTTON_ENTER_LOCATOR = ('xpath', '//button[@id="passp:sign-in"]')
    FIELD_LOGIN_LOCATOR = (
        'xpath', '//div[contains(@class,"Auth")]//span[@class="CurrentAccount-displayName"]'
        )
    INPUT_PASSWORD_LOCATOR = ('xpath', '//input[@id="passp-field-passwd"]')
    CONTINUE_BUTTON_LOCATOR = ('xpath', '//button[@id="passp:sign-in"]')
    PREV_STEP_BUTTON_LOCATOR = (
        'xpath', '//a[contains(@class, "PreviousStepButton ")]'
        )

    # functions:
    @allure.step('Ввести логин или пароль')
    def enter_login_data(self, login_or_email: str):
        self.wait.until(
            EC.element_to_be_clickable((self.INPUT_LOGIN_LOCATOR))
            ).send_keys(login_or_email)

    @allure.step('Нажать кнопку "Войти"')
    def enter_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.BUTTON_ENTER_LOCATOR))
            ).click()

    @allure.step('Ввести данные для поиска')
    def get_login_data(self) -> str:
        data = self.wait.until(
            EC.visibility_of_element_located((self.FIELD_LOGIN_LOCATOR))
            )
        return data.text

    @allure.step('Ввести пароль - {password}')
    def enter_password(self, password: str):
        self.wait.until(
            EC.element_to_be_clickable((self.INPUT_PASSWORD_LOCATOR))
            ).send_keys(password)

    @allure.step('Нажить кнопку "Продолжить"')
    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable((self.CONTINUE_BUTTON_LOCATOR))
            ).click()

    @allure.step('Нажить кнопку "Вернуться обратно"')
    def click_prev_step_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.PREV_STEP_BUTTON_LOCATOR))
            ).click()
