from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.online_cinema_page import OnlineCinemaPage
from time import sleep
import allure
from userdata.DataProvider import DataProvider


def test_auth(driver):
    data = DataProvider().getUI('login')
    main = MainPage(driver)
    login = LoginPage(driver)

    main.open_the_page()
    # main.page_is_opened()
    main.click_login_button()
    login.enter_login_data(login_or_email=data)
    login.enter_login_button()

    assert data == login.get_login_data()


def test_unauthorization(driver):
    online = OnlineCinemaPage(driver)
    login = LoginPage(driver)

    online.open_the_page()
    before_url = online.get_current_url()
    # online.is_opened()  # ошибка если капча
    online.click_subscribe_button()
    login.click_prev_step_button()
    after_url = online.get_current_url()

    assert before_url == after_url  # ошибка если капча


@allure.story('Отмена авторизации после добавления фильма в избранное без регистрации')
@allure.description('Тест падает из-за бага, страница не возвращается обратно')
def test_unauthorization_via_favorites(driver):
    online = OnlineCinemaPage(driver)
    login = LoginPage(driver)

    online.open_the_page()
    before_url = online.get_current_url()
    online.click_movie()
    online.click_bookmark()
    login.click_prev_step_button()
    after_url = online.get_current_url()

    with allure.step('Сравнить переменные'):
        assert before_url == after_url, 'кнопка возврата не работает'


@allure.story('Тестирование функции быстрого поиска')
@allure.description('В поисковую строку введем данные и проверим что поиск находит подсказки по симовлам')
def test_fast_search(driver):
    main = MainPage(driver)

    main.open_the_page()
