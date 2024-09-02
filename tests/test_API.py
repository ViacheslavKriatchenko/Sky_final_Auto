from api.cinema import Cinema
import pytest


@pytest.mark.positive
def test_search_movie_by_id():
    cinema = Cinema()
    id = 444

    response = cinema.search_movie_by_id(id)

    assert id == response['id']


@pytest.mark.negative
def test_search_movie_by_false_id():
    cinema = Cinema()
    id = 100

    response = cinema.search_movie_by_id(id)

    assert response['statusCode'] == 400
    assert response['message'][0] == "Значение поля id должно быть в диапазоне от 250 до 7000000!"


def test_search_movie_by_name():
    cinema = Cinema()

    response = cinema.search_movie_by_name(movie_name='Тер')
    len_response = len(response['docs'])
    for i in range(0, 10):
        print(response['docs'][i]['name'])
    # print(response['docs'][0])
    assert len_response == 10
