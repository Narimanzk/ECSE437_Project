from typing import List

import pandas as pd

from src.client.postgres_client import PostgresClient
from src.model.movie import Movie
from src.repository.mapper.mapper import Mapper


class MovieRepository:

    def __init__(self, postgres_client: PostgresClient):
        self.__postgres_client = postgres_client

    def get_movie(self, title: str) -> Movie:
        movie_df: pd.DataFrame = self.__postgres_client.retrieve_movie(title)
        if movie_df.empty:
            return None
        return Mapper.convert_dataframe_to_movie(movie_df.iloc[0])

    def get_movies_by_titles(self, movie_titles: List[str]) -> List[Movie]:
        movies_df: pd.DataFrame = self.__postgres_client.retrieve_movies(movie_titles)
        movie_list: List[Movie] = list(movies_df.apply(Mapper.convert_dataframe_to_movie, axis=1))
        return movie_list

    def save(self, movie: Movie) -> None:
        movie_df: pd.DataFrame = Mapper.convert_movie_to_dataframe(movie)
        self.__postgres_client.save(movie_df)