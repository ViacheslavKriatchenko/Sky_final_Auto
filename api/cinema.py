import requests
import allure


class Cinema:

    HOST_URL = "https://api.kinopoisk.dev/"
    TOKEN = "0HNA0QZ-VXA4T12-HHKD3SB-DTRX68P"

    my_header = {"X-API-KEY": TOKEN}

    def search_movie_by_id(self, id: int) -> dict:
        response = requests.get(
            url=f"{self.HOST_URL}/v1.4/movie/{id}", headers=self.my_header
        )
        return response.json()

    @allure.step("Поиск фильма по имени {movie_name}")
    def search_movie_by_name(
        self, movie_name: str, page_number=1, elements_number=10
    ) -> dict:
        response = requests.get(
            url=f"{self.HOST_URL}/v1.4/movie/search",
            headers=self.my_header,
            params={
                "page": page_number,
                "limit": elements_number,
                "query": movie_name}
        )
        return response.json()

