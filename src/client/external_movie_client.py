from typing import List

import requests

from src.config.external_movies_client_config import ExternalMovieClientConfig


class ExternalMovieClient:

    def __init__(self, config: ExternalMovieClientConfig):
        self.__config = config

    def get_all_movies_titles(self) -> List[str]:
        fetch_all_ids_url: str = f"{self.__config.url}:{self.__config.port}" + "/fetch-all-titles"
        response = requests.get(fetch_all_ids_url)
        return response.json()["movie_titles"]