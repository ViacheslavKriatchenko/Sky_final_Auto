from api.cinema import Cinema
import pytest
import allure
from userdata.DataProvider import DataProvider


@allure.testcase('Тело ответа возвращает запрашиваемый id')
@allure.description('Отправим запрос с валидным id и проверим что тело вернет ответ с нужным параметром')
@pytest.mark.positive
def test_search_movie_by_id():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema(HOST_URL="https://api.kinopoisk.dev/", TOKEN=TOKEN)
    ID = DataProvider().getAPI_int('MOVIE_ID_valid')

    response = cinema.search_movie_by_id(id=ID)
    with allure.step('Сравнение запрашиваемого и полученного ID'):
        assert ID == response['id'], "Ошибка данных"


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


def test_search_movie_by_name():
    TOKEN = DataProvider().getAPI('TOKEN')
    cinema = Cinema("https://api.kinopoisk.dev/", TOKEN=TOKEN)

    response = cinema.search_movie_by_name(movie_name='Тер')
    len_response = len(response['docs'])
    for i in range(0, 10):
        print(response['docs'][i]['name'])
    # print(response['docs'][0])
    assert len_response == 10
