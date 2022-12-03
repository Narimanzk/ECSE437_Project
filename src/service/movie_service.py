from typing import List

from src.client.external_movie_client import ExternalMovieClient
from src.model.movie import Movie
from src.repository.movie_repository import MovieRepository
from src.validation.movie_validation_service import MovieValidationService


class MovieService:

    def __init__(self,
                 movie_repository: MovieRepository,
                 external_movie_client: ExternalMovieClient):
        self.__movie_repository = movie_repository
        self.__external_movie_client = external_movie_client

    def get_movie_by_title(self, title: str) -> Movie:
        MovieValidationService.validate_title(title)
        movie: Movie = self.__movie_repository.get_movie(title)
        return movie

    def get_all_movies(self) -> List[Movie]:
        movie_titles: List[str] = self.__external_movie_client.get_all_movies_titles()
        movie_list: List[Movie] = self.__movie_repository.get_movies_by_titles(movie_titles)
        return movie_list

    def save(self, title: str, director: str, year: int, genre: str) -> None:
        movie: Movie = Movie(title=title,
                            director=director,
                            year=year,
                            genre=genre)
        self.__movie_repository.save(movie)