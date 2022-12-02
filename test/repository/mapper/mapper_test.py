import unittest

import pandas as pd

from src.model.movie import Movie
from src.repository.mapper.mapper import Mapper


class MapperTest(unittest.TestCase):

    def test_should_convert_dataframe_to_movie(self):
        # given
        movie_df = pd.DataFrame({'title': ['matrix'],
                                    'director': ['wachowski'],
                                    'year': [1999],
                                    'genre': ['action']})

        # when
        movie = Mapper.convert_dataframe_to_movie(movie_df.iloc[0])

        # then
        self.assertIsNotNone(movie)
        self.assertEqual(movie.title, 'matrix')
        self.assertEqual(movie.director, 'wachowski')
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.genre, 'action')

    def test_should_convert_movie_to_dataframe(self):
        # given
        movie = movie(title='matrix',
                            director='wachowski',
                            year=1999,
                            genre='action')

        # when
        movie_df = Mapper.convert_movie_to_dataframe(movie=movie)

        # then
        self.assertIsNotNone(movie_df)
        self.assertEqual(movie_df.iloc[0]['title'], 'matrix')
        self.assertEqual(movie_df.iloc[0]['director'], 'wachowski')
        self.assertEqual(movie_df.iloc[0]['year'], 1999)
        self.assertEqual(movie_df.iloc[0]['genre'], 'action')