from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.online_cinema_page import OnlineCinemaPage
from time import sleep
import allure
from userdata.DataProvider import DataProvider


def test_auth(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        data = DataProvider().getUI('LOGIN')
        main = MainPage(driver)
        login = LoginPage(driver)

    main.open_the_page()
    # main.page_is_opened()  # ошибка если капча
    main.click_login_button()
    login.enter_login_data(login_or_email=data)
    login.enter_login_button()

    with allure.step('Проверка. Сравниваем введенный логин с записью в поле'):
        assert data == login.get_login_data()


def test_unauthorization(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        online = OnlineCinemaPage(driver)
        login = LoginPage(driver)

    online.open_the_page()
    before_url = online.get_current_url()
    # online.is_opened()  # ошибка если капча
    online.click_subscribe_button()
    login.click_prev_step_button()
    after_url = online.get_current_url()

    with allure.step('Проверка. Сравниваем адреса - страница вернулась обратно'):
        assert before_url == after_url  # ошибка если капча


@allure.title('Отмена авторизации после добавления фильма в избранное без регистрации')
@allure.description('Тест падает из-за бага, страница не возвращается обратно')
def test_unauthorization_via_favorites(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        online = OnlineCinemaPage(driver)
        login = LoginPage(driver)

    online.open_the_page()
    before_url = online.get_current_url()
    online.click_movie()
    online.click_bookmark()
    login.click_prev_step_button()  # вставить скриншот
    after_url = online.get_current_url()

    with allure.step('Проверка. Сравниваем адреса - страница вернулась обратно'):
        assert before_url == after_url, 'кнопка возврата не работает'


@allure.story('Тестирование функции быстрого поиска')
@allure.description('В поисковую строку введем данные и проверим что поиск находит подсказки по симовлам')
def test_fast_search(driver):
    main = MainPage(driver)

    main.open_the_page()


def test_click_menu_button(driver):
    main = MainPage(driver)

    main.open_the_page()
    sleep(10)
    main.click_menu_button()
