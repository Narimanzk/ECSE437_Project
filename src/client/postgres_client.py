from typing import List

import pandas as pd
import psycopg2

from src.config.postgres_client_config import PostgresClientConfig


class PostgresClient:

    def __init__(self, postgres_client_config: PostgresClientConfig):
        self.__config = postgres_client_config

    def retrieve_movie(self, title: str) -> pd.DataFrame:
        connection = self.__create_connection()
        query: str = f"select title, director, year, genre from test.movie where title = '{title}';"
        return pd.read_sql(query, connection)

    def retrieve_movies(self, movie_titles: List[str]) -> pd.DataFrame:
        connection = self.__create_connection()
        query: str = f"select title, director, year, genre from test.movie where title in {tuple(movie_titles)};"
        return pd.read_sql(query, connection)

    def save(self, movie_df: pd.DataFrame) -> None:
        connection = self.__create_connection()
        cursor = connection.cursor()
        query: str = """
            INSERT INTO test.movie (title, director, year, genre) values('%s','%s','%s', '%s');
            """ % (movie_df.iloc[0]['title'],
                   movie_df.iloc[0]['director'],
                   movie_df.iloc[0]['year'],
                   movie_df.iloc[0]['genre'])
        try:
            cursor.execute(query)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            connection.rollback()
            cursor.close()
        cursor.close()

    def __create_connection(self):
        return psycopg2.connect(
            host=self.__config.url,
            port=self.__config.port,
            database=self.__config.database,
            user=self.__config.user_name,
            password=self.__config.password
        )