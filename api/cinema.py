import requests
import allure


class Cinema:

    def __init__(self, HOST_URL: str, TOKEN: str) -> None:
        self.HOST_URL = HOST_URL
        self.TOKEN = TOKEN

    @allure.step("Поиск фильма по {id}")
    def search_movie_by_id(
        self,
        id: int
    ) -> dict:

        response = requests.get(
            url=f"{self.HOST_URL}/v1.4/movie/{id}",
            headers={
                "X-API-KEY": self.TOKEN
            }
        )
        return response.json()

    @allure.step("Поиск фильма по имени {movie_name}")
    def search_movie_by_name(
        self,
        movie_name: str,
        page_number=1,
        elements_number=10
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

    @allure.step("Получить список стран, жанров и т.д.")
    def get_list_movie_info(self, field: str) -> list:
        response = requests.get(
            url=f"{self.HOST_URL}/v1/movie/possible-values-by-field",
            headers={
                "X-API-KEY": self.TOKEN
            },
            params={
                "field": field
            }
        )
        return response.json()

    @allure.step("Универсальный поиск с фильтрами")
    def universal_search_filter(
            self,
            year: str,
            rating_imdb: str,
            genres_name: str = None,
            page=1,
            limit=10  # Union[str, float] / ошибка дефолтных значений
    ) -> dict:

        response = requests.get(
            url=f"{self.HOST_URL}/v1/movie",
            headers={
                "X-API-KEY": self.TOKEN
            },
            params={
                "page": page,
                "limit": limit,
                "year": year,
                "genres.name": genres_name,
                "rating.imdb": rating_imdb
            }
        )
        return response.json()
