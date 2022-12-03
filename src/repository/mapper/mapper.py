import pandas as pd

from src.model.movie import Movie


class Mapper:

    @staticmethod
    def convert_dataframe_to_movie(movie_df: pd.Series) -> Movie:
        return Movie(title=movie_df['title'],
                        director=movie_df['director'],
                        year=movie_df['year'],
                        genre=movie_df['genre'])

    @classmethod
    def convert_movie_to_dataframe(cls, movie: Movie) -> pd.DataFrame:
        return pd.DataFrame({'title': [movie.title],
                             'director': [movie.director],
                             'year': [movie.year],
                             'genre': [movie.genre]})