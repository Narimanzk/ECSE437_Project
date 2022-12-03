import unittest
from unittest.mock import Mock

import pandas as pd

from src.repository.movie_repository import MovieRepository


class MovieRepositoryTest(unittest.TestCase):

    def test_should_get_movie(self):
        # given
        client = Mock()
        client.retrieve_movie.return_value = pd.DataFrame({'title': ['matrix'],
                                                              'director': ['wachowski'],
                                                              'year': [1999],
                                                              'genre': ['action']})
        movie_repository = MovieRepository(postgres_client=client)

        # when
        movie = movie_repository.get_movie('matrix')

        # then
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'matrix')
        self.assertEqual(movie.director, 'wachowski')
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.genre, 'action')

    def test_should_get_movies(self):
        # given
        client = Mock()
        client.retrieve_movies.return_value = pd.DataFrame({'title': ['matrix', 'goodfellas', 'se7en'],
                                                               'director': ['wachowski', 'scorsese', 'fincher'],
                                                               'year': [1999, 1990, 1995],
                                                               'genre': ['action', 'biography', 'crime']})

        movie_repository = MovieRepository(postgres_client=client)

        # when
        movies = movie_repository.get_movies_by_titles(['matrix', 'goodfellas', 'se7en'])

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