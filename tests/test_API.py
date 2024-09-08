from api.cinema import Cinema
import pytest
import allure
from userdata.DataProvider import DataProvider
from config.ConfigProvider import ConfigProvider
from random import randint


@allure.issue('api-1')
@allure.title('Тело ответа возвращает запрашиваемый id')
@allure.description('Отправим запрос с валидным id и проверим, '
                    'что тело вернет ответ с нужным параметром')
@pytest.mark.positive
def test_search_movie_by_id(get_token):
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = get_token  # через фикстуру
        # TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(
            HOST_URL=ConfigProvider().get(section='api', prop='API_HOST'),
            TOKEN=TOKEN
            )
        ID = DataProvider().getAPI_int('MOVIE_ID_valid')

    with allure.step('Функциональный блок'):
        response = cinema.search_movie_by_id(id=ID)

    with allure.step('Проверка запрашиваемого и полученного ID'):
        assert ID == response['id'], "Ошибка данных"
    with allure.step('Проверка названия фильма полученного по ID'):
        assert response['alternativeName'] == DataProvider().getAPI('ASSERT_MOVIE_NAME')  # ошибка кодировки кирилица


@allure.issue('api-2')
@allure.title('Тело ответа возвращает ошибку при невалидном id')
@allure.description('Отправим запрос с невалидным id и проверим, '
                    'что тело вернет ошибку')
@pytest.mark.negative
def test_search_movie_by_false_id():
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(
            HOST_URL=ConfigProvider().get(section='api', prop='API_HOST'),
            TOKEN=TOKEN
            )
        ID = DataProvider().getAPI_int('MOVIE_ID_not_valid')

    with allure.step('Функциональный блок'):
        response = cinema.search_movie_by_id(id=ID)

    with allure.step('Проверка. Сверяем код ответа и текст тела'):
        assert response['statusCode'] == 400
        assert (
            response["message"][0]
            == "Значение поля id должно быть в диапазоне от 250 до 7000000!"
        )


@allure.issue('api-3')
@allure.title('Тело ответа возвращает фильмы содержащие искомое слово')
@allure.description('Отправим запрос со словом и проверим, '
                    'что тело вернет список фильмов, '
                    'названия которых содержат введенное значение')
@pytest.mark.positive
def test_search_movie_by_name():
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(
            HOST_URL=ConfigProvider().get(section='api', prop='API_HOST'),
            TOKEN=TOKEN
            )
        movie_name = DataProvider().getAPI('MOVIE_NAME')

    with allure.step('Функциональный блок'):
        response = cinema.search_movie_by_name(
            movie_name=DataProvider().getAPI('MOVIE_NAME'))
        len_response = len(response['docs'])
        with allure.step('Создаем список названий полученных фильмов'):
            movie_name_list = []
            for i in range(0, 10):
                film = response['docs'][i]['alternativeName']
                movie_name_list.append(film)

    assert len_response <= 10
    for movie in movie_name_list:
        with allure.step('Проверка искомого слова в списке'):
            assert movie_name in movie, "ошибка поисковой системы"


@allure.issue('api-4')
@allure.title('Тело ответа возвращает запрашиваемый список данных')
@allure.description('Отправим запрос с параметром и проверим, '
                    'что тело вернет ответ с нужным списком')
@pytest.mark.positive
def test_get_list_movie_info():
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(
            HOST_URL=ConfigProvider().get(section='api', prop='API_HOST'),
            TOKEN=TOKEN
            )
        FIELD = DataProvider().getAPI('FIELD')[randint(0, 5)]  # берем рандомный field

    with allure.step('Функциональный блок'):
        response = cinema.get_list_movie_info(field=FIELD)
    if FIELD == "":
        with allure.step(
            "Проверка. Если пустые данные, "
            "проверить что вернется словарь и будет ошибка"
        ):
            assert type(response) is dict
            assert response["statusCode"] == 400 and response["error"] == "Bad Request"
    else:
        with allure.step(
            "Проверка. Проверить, "
            "что возвращается список содержащий ключи 'name' и 'slug'"
        ):
            assert type(response) is list
            assert 'name' in response[0]
            assert 'slug' in response[0]


@allure.issue('api-5')
@allure.title('Тело ответа возвращает запрашиваемый список данных')
@allure.description('')
def test_universal_search_filter():
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(HOST_URL="https://api.kinopoisk.dev/", TOKEN=TOKEN)

    with allure.step('Функциональный блок'):
        response = cinema.universal_search_filter(
            year=DataProvider().getAPI('YEAR'),
            # genres_name=DataProvider().getAPI('GENRES.NAME'), ошибка кодировки, нельзя передать жанры
            rating_imdb=DataProvider().getAPI('RAITING_IMDB')
        )

    with allure.step('Проверка. Тело вернулось как словарь'):
        assert type(response) is dict


@allure.issue('api-6')
@allure.title('Тело ответа возвращает запрашиваемый список данных персоны')
@allure.description('Отправим имя персоны для поиска')
def test_search_actor():
    with allure.step('Наследуем переменным классы, запрашиваем данные'):
        TOKEN = DataProvider().getAPI('TOKEN')
        cinema = Cinema(HOST_URL="https://api.kinopoisk.dev/", TOKEN=TOKEN)
        actor_name = DataProvider().getAPI('ACTOR_NAME')

    with allure.step('Функциональный блок'):
        response = cinema.search_actor(actor_name=actor_name)

    with allure.step(
        "Проверка. Получаем словарь и первая запись "
        "содержит данные по искомому имени"
    ):
        assert type(response) is dict
        assert response['docs'][0]['enName'] == actor_name
