import unittest
from unittest.mock import Mock

from src.model.movie import Movie
from src.service.movie_service import MovieService


class MovieServiceTest(unittest.TestCase):

    def test_should_get_movie_by_title(self):
        # given
        movie_repository = Mock()
        movie_repository.get_movie.return_value = Movie(title='matrix',
                                                                 director='wachowski',
                                                                 year=1999,
                                                                 genre='action')
        external_movies_client = Mock()

        movie_service = MovieService(movie_repository=movie_repository,
                                           external_movie_client=external_movies_client)

        # when
        movie = movie_service.get_movie_by_title('matrix')

        # then
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'matrix')
        self.assertEqual(movie.director, 'wachowski')
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.genre, 'action')

    def test_should_raise_an_exception_when_title_is_invalid(self):
        # given
        movie_repository = Mock()
        external_movies_client = Mock()

        movie_service = MovieService(movie_repository=movie_repository,
                                           external_movie_client=external_movies_client)

        # when
        with self.assertRaises(Exception) as context:
            movie_service.get_movie_by_title('matrics')

        # then
        self.assertTrue('title is invalid.' in str(context.exception))