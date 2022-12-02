from typing import List

from fastapi import FastAPI

from src.model.movie import Movie
from src.service.movie_service import MovieService


class MovieRestApi(FastAPI):

    def __init__(self, movie_service: MovieService):
        super(MovieRestApi, self).__init__()

        @self.get("/api/v1/fetch-by-title")
        def fetch_movie_by_title(title: str) -> Movie:
            return movie_service.get_movie_by_title(title)

        @self.get("/api/v1/fetch-all")
        def fetch_all_movies() -> List[Movie]:
            return movie_service.get_all_movies()

        @self.post("/api/v1/save-movie")
        def save_movie(title: str, director: str, year: int, genre: str) -> None:
            return movie_service.save(title=title,
                                         director=director,
                                         year=year,
                                         genre=genre)
