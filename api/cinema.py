import requests
import allure


class Cinema:

    def __init__(self, HOST_URL: str, TOKEN: str) -> None:
        self.HOST_URL = HOST_URL
        self.TOKEN = TOKEN

    @allure.step('Поиск фильма по {id}')
    def search_movie_by_id(self, id: int) -> dict:
        response = requests.get(
            url=f"{self.HOST_URL}/v1.4/movie/{id}",
            headers={
                "X-API-KEY": self.TOKEN
            }
        )
        return response.json()

    @allure.step("Поиск фильма по имени {movie_name}")
    def search_movie_by_name(
        self, movie_name: str, page_number=1, elements_number=10
    ) -> dict:
        response = requests.get(
            url=f"{self.HOST_URL}/v1.4/movie/search",
            headers={
                "X-API-KEY": self.TOKEN
            },
            params={
                "page": page_number,
                "limit": elements_number,
                "query": movie_name
            }
        )
        return response.json()
