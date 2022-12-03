import unittest

import pandas as pd

from src.client.postgres_client import PostgresClient
from test.resources.abstract_integration_test_class import AbstractIntegrationTestClass


class PostgresClientIntegrationTest(unittest.TestCase, AbstractIntegrationTestClass):

    @classmethod
    def setUpClass(cls) -> None:
        cls.setup()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down()

    def test_should_retrieve_movie(self):
        # given
        postgres_client_config = self.postgres_client_config

        postgres_client = PostgresClient(postgres_client_config)

        # when
        movie_df = postgres_client.retrieve_movie('matrix')

        # then
        self.assertIsNotNone(movie_df)
        self.assertEqual(movie_df.iloc[0]['title'], 'matrix')
        self.assertEqual(movie_df.iloc[0]['director'], 'wachowski')
        self.assertEqual(movie_df.iloc[0]['year'], 1999)
        self.assertEqual(movie_df.iloc[0]['genre'], 'action')

    def test_should_retrieve_movies(self):
        # given
        postgres_client_config = self.postgres_client_config

        postgres_client = PostgresClient(postgres_client_config)

        # when
        movies_df = postgres_client.retrieve_movies(['matrix', 'goodfellas', 'se7en'])

        self.assertIsNotNone(movies_df)
        self.assertEqual(len(movies_df), 3)

        self.assertEqual(movies_df.iloc[0]['title'], 'matrix')
        self.assertEqual(movies_df.iloc[0]['director'], 'wachowski')
        self.assertEqual(movies_df.iloc[0]['year'], 1999)
        self.assertEqual(movies_df.iloc[0]['genre'], 'action')

        self.assertEqual(movies_df.iloc[1]['title'], 'goodfellas')
        self.assertEqual(movies_df.iloc[1]['director'], 'scorsese')
        self.assertEqual(movies_df.iloc[1]['year'], 1990)
        self.assertEqual(movies_df.iloc[1]['genre'], 'biography')

        self.assertEqual(movies_df.iloc[2]['title'], 'se7en')
        self.assertEqual(movies_df.iloc[2]['director'], 'fincher')
        self.assertEqual(movies_df.iloc[2]['year'], 1995)
        self.assertEqual(movies_df.iloc[2]['genre'], 'crime')

    def test_should_save_movie(self):
        # given
        movie_title = 'Superbad'
        movie_director = 'Greg Mottola'
        movie_year = 2007
        movie_genre = 'comedy'
        movie_df = pd.DataFrame({'title': [movie_title],
                                    'director': [movie_director],
                                    'year': [movie_year],
                                    'genre': [movie_genre]})

        postgres_client_config = self.postgres_client_config
        postgres_client = PostgresClient(postgres_client_config)

        # when
        postgres_client.save(movie_df)

        # then
        connection = self.create_connection()
        query = f"select * from test.movie where title = '{movie_title}' " \
                f"and director = '{movie_director}' " \
                f"and year = {movie_year} " \
                f"and genre = '{movie_genre}';"

        movie_fetched = pd.read_sql(query, con=connection)

        self.assertIsNotNone(movie_fetched)
        self.assertEqual(movie_fetched.iloc[0]['tile'], 'Superbad')
        self.assertEqual(movie_fetched.iloc[0]['director'], 'Greg Mottola')
        self.assertEqual(movie_fetched.iloc[0]['year'], 2007)
        self.assertEqual(movie_fetched.iloc[0]['genre'], 'comedy')