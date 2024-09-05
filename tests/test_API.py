from api.cinema import Cinema
import pytest
import allure
from userdata.DataProvider import DataProvider
from config.ConfigProvider import ConfigProvider
from random import randint


@allure.testcase('Тело ответа возвращает запрашиваемый id')
@allure.description('Отправим запрос с валидным id и проверим,'
                    'что тело вернет ответ с нужным параметром')
@pytest.mark.positive
def test_search_movie_by_id():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema(
        HOST_URL=ConfigProvider().get(section='api', prop='API_HOST'),
        TOKEN=TOKEN
        )
    ID = DataProvider().getAPI_int('MOVIE_ID_valid')

    response = cinema.search_movie_by_id(id=ID)
    with allure.step('Сравнение запрашиваемого и полученного ID'):
        assert ID == response['id'], "Ошибка данных"


@allure.testcase('Тело ответа возвращает ошибку при невалидном id')
@allure.description('Отправим запрос с невалидным id и проверим,'
                    'что тело вернет ошибку')
@pytest.mark.negative
def test_search_movie_by_false_id():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema("https://api.kinopoisk.dev/", TOKEN=TOKEN)
    ID = DataProvider().getAPI_int('MOVIE_ID_not_valid')

    response = cinema.search_movie_by_id(id=ID)

    assert response['statusCode'] == 400
    assert (
        response["message"][0]
        == "Значение поля id должно быть в диапазоне от 250 до 7000000!"
    )


@allure.testcase('Тело ответа возвращает фильмы содержащие искомое слово')
@allure.description('Отправим запрос со словом и проверим,'
                    'что тело вернет список фильмов,'
                    'названия которых содержат введенное значение')
@pytest.mark.positive
def test_search_movie_by_name():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema("https://api.kinopoisk.dev/", TOKEN=TOKEN)

    response = cinema.search_movie_by_name(movie_name='Тер')
    len_response = len(response['docs'])
    movie_name_list = []
    for i in range(0, 10):
        a = response['docs'][i]['name']
        movie_name_list.append(a)
    print(response['docs'][0])
    print(movie_name_list)
    assert len_response == 10
    for movie in movie_name_list:
        assert "Тер" in movie, "ошибка поисковой системы"


@allure.testcase('Тело ответа возвращает запрашиваемый список данных')
@allure.description('Отправим запрос с параметром и проверим,'
                    'что тело вернет ответ с нужным списком')
@pytest.mark.positive
def test_get_list_movie_info():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema("https://api.kinopoisk.dev/", TOKEN=TOKEN)
    FIELD = DataProvider().getAPI('FIELD')[randint(0, 5)]  # ошибка из-за выбора

    response = cinema.get_list_movie_info(field=FIELD)

    if FIELD == "":
        with allure.step("Если пустые данные, проверить что вернется ошибка"):
            assert type(response) is dict
            assert response["statusCode"] == 400 and response["error"] == "Bad Request"
    else:
        assert type(response) is list
        assert response[0]['name'] == 'аниме'  # переделать


def test_universal_search_filter():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema(HOST_URL="https://api.kinopoisk.dev/", TOKEN=TOKEN)

    response = cinema.universal_search_filter(
        year=DataProvider().getAPI('YEAR'),
        # genres_name=DataProvider().getAPI('GENRES.NAME'),
        rating_imdb=DataProvider().getAPI('RAITING_IMDB')
    )

    assert type(response) is dict
