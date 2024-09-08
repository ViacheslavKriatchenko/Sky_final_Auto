from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.online_cinema_page import OnlineCinemaPage
from time import sleep  # для отладки
import allure
from userdata.DataProvider import DataProvider
from config.ConfigProvider import ConfigProvider


@allure.issue('ui-1')
@allure.title('Подтверждение пользователя')
@allure.description('Нажмем кнопку Войти на главной странице,'
                    'введем логин и нажмем Войти, и проверим,'
                    'что введенные данные соответствию полю пользователю'
                    )
def test_auth(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        data = DataProvider().getUI('LOGIN')
        main = MainPage(driver)
        login = LoginPage(driver)

    with allure.step('Функциональный блок'):
        main.open_the_page()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # отладка капчи вручную
        # main.page_is_opened()  # ошибка если капча
        main.click_login_button()
        login.enter_login_data(login_or_email=data)
        login.enter_login_button()

    with allure.step('Проверка. Сравниваем введенный логин с записью в поле'):
        assert data == login.get_login_data()


@allure.issue('ui-2')
@allure.title('Работа кнопки отмена в разведеле авторизация')
@allure.description('На главной странице нажмем "Войти" и'
                    'потом в окне авторизации нажмем стрелку "Назад"')
def test_unauthorization(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        online = OnlineCinemaPage(driver)
        login = LoginPage(driver)

    with allure.step('Функциональный блок'):
        online.open_the_page()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # отладка капчи вручную
        before_url = online.get_current_url()
        # online.is_opened()  # ошибка если капча
        online.click_subscribe_button()
        login.click_prev_step_button()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # отладка капчи вручную
        after_url = online.get_current_url()

    with allure.step('Проверка. Сравниваем адреса - страница вернулась обратно'):
        assert before_url == after_url, 'ошибка в работе сайта'  # ошибка если капча


@allure.issue('ui-3')
@allure.label('https://drive.google.com/file/d/1TLHPfAsag8OUjLTSDu_Bj3yUOzLnqMCT/view?usp=sharing', 'Баг')
@allure.title('Отмена авторизации после добавления фильма в избранное без регистрации')
@allure.description('Тест падает из-за бага, страница не возвращается обратно')
def test_unauthorization_via_favorites(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        online = OnlineCinemaPage(driver)
        login = LoginPage(driver)

    with allure.step('Функциональный блок'):
        online.open_the_page()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # отладка капчи вручную
        before_url = online.get_current_url()
        online.click_movie()
        online.click_bookmark()
        login.click_prev_step_button()
        login.save_screenshot()
        after_url = online.get_current_url()

    with allure.step('Проверка. Сравниваем адреса - страница вернулась обратно'):
        assert before_url == after_url, 'кнопка возврата не работает'


@allure.issue('ui-4')
@allure.title('Тестирование функции быстрого поиска')
@allure.description('В поисковую строку введем данные и запросим их')
def test_fast_search(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        main = MainPage(driver)
        search = DataProvider().getUI(prop="SEARCH_MOVIE")

    with allure.step('Функциональный блок'):
        main.open_the_page()
        sleep(ConfigProvider().getint(section='common', prop='sleep'))  # отладка капчи вручную
        result = main.enter_search_data(data=search)

    with allure.step(
        'Проверка. Запрашиваемая информация содержится в поисковой выдаче'
    ):
        assert search in result


@allure.issue('ui-5')
@allure.title('Тестирование функции быстрого поиска')
@allure.description('В поисковую строку введем данные и /////')
def test_movie_selection(driver):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        main = MainPage(driver)

    with allure.step('Функциональный блок'):
        main.open_the_page()
        sleep(15)
        text_search, text_find = main.movie_selection()
    with allure.step('Проверка. Перешли на страницу с выбранным фильмом'):
        assert text_search == text_find
