import unittest

import pandas as pd

from src.client.external_movie_client import ExternalMovieClient
from src.client.postgres_client import PostgresClient
from src.config.external_movies_client_config import ExternalMovieClientConfig
from src.config.postgres_client_config import PostgresClientConfig
from src.repository.movie_repository import MovieRepository
from src.service.movie_service import MovieService
from test.resources.abstract_integration_test_class import AbstractIntegrationTestClass


class MovieServiceIntegrationTest(unittest.TestCase, AbstractIntegrationTestClass):

    @classmethod
    def setUpClass(cls) -> None:
        cls.setup()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down()

    def test_should_get_movie_by_name(self):
        # given
        movie_service = self.__generate_movie_service()

        # when
        movie = movie_service.get_movie_by_title("matrix")

        # then
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'matrix')
        self.assertEqual(movie.director, 'wachowski')
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.genre, 'action')

    def test_should_raise_an_exception_when_title_is_invalid(self):
        # given
        movie_service = self.__generate_movie_service()

        # when
        with self.assertRaises(Exception) as context:
            movie = movie_service.get_movie_by_title("matrix46")

        # then
        self.assertTrue("Title is invalid." in str(context.exception))

    def test_should_get_all_movies(self):
        # given
        movie_service = self.__generate_movie_service()

        # when
        movies = movie_service.get_all_movies()

        # then
        self.assertIsNotNone(movies)
        self.assertEqual(len(movies), 3)

        self.assertEqual(movies[0].title, 'matrix')
        self.assertEqual(movies[0].director, 'wachowski')
        self.assertEqual(movies[0].year, 1999)
        self.assertEqual(movies[0].genre, 'action')

        self.assertEqual(movies[1].title, 'goodfellas')
        self.assertEqual(movies[1].director, 'scorsese')
        self.assertEqual(movies[1].year, 1990)
        self.assertEqual(movies[1].genre, 'biography')

        self.assertEqual(movies[2].title, 'se7en')
        self.assertEqual(movies[2].director, 'fincher')
        self.assertEqual(movies[2].year, 1995)
        self.assertEqual(movies[2].genre, 'crime')

    def test_should_save_movie(self):
        # given
        title = 'Superbad'
        director = 'Greg Mottola'
        year = 2007
        genre = 'comedy'

        movie_service = self.__generate_movie_service()

        # when
        movie_service.save(title=title,
                              director=director,
                              year=year,
                              genre=genre)

        # then
        connection = self.create_connection()
        query = f"select * from test.movie where title = '{title}' " \
                f"and director = '{director}' " \
                f"and year = '{year}' " \
                f"and genre = '{genre}' "

        movie_fetched = pd.read_sql(query, con=connection)

        self.assertEqual(movie_fetched.iloc[0]['title'], title)
        self.assertEqual(movie_fetched.iloc[0]['director'], director)
        self.assertEqual(movie_fetched.iloc[0]['year'], year)
        self.assertEqual(movie_fetched.iloc[0]['genre'], genre)

    def __generate_movie_service(self) -> MovieService:
        postgres_url = "localhost"
        postgres_port = "5433"
        postgres_database = "movieApp"
        postgres_user_name = "rio"
        postgres_password = "riotinto"
        external_client_url = "http://localhost"
        external_client_port = 8081
        postgres_client_config = PostgresClientConfig(url=postgres_url,
                                                      port=postgres_port,
                                                      database=postgres_database,
                                                      user_name=postgres_user_name,
                                                      password=postgres_password)
        postgres_client = PostgresClient(postgres_client_config)
        movie_repository = MovieRepository(postgres_client=postgres_client)
        external_movie_client_config = ExternalMovieClientConfig(url=external_client_url, port=external_client_port)
        external_movie_client = ExternalMovieClient(external_movie_client_config)
        movie_service = MovieService(movie_repository=movie_repository,
                                           external_movie_client=external_movie_client)
        return movie_service