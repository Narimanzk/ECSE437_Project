import unittest

from src.client.external_movie_client import ExternalMovieClient
from src.config.external_movies_client_config import ExternalMovieClientConfig
from test.resources.abstract_integration_test_class import AbstractIntegrationTestClass


class ExternalMovieClientIntegrationTest(unittest.TestCase, AbstractIntegrationTestClass):

    @classmethod
    def setUpClass(cls) -> None:
        cls.setup()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.tear_down()

    def test_should_get_all_movie_titles(self):
        # given
        external_movie_client_url = "http://localhost"
        external_movie_client_port = 8081
        config = ExternalMovieClientConfig(url=external_movie_client_url, port=external_movie_client_port)
        external_movie_client = ExternalMovieClient(config)

        # when
        movie_titles = external_movie_client.get_all_movies_titles()

        # then
        self.assertIsNotNone(movie_titles)
        self.assertListEqual(movie_titles, ['matrix', 'goodfellas', 'se7en'])