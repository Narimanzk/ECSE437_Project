import unittest

import pandas as pd

from test.resources.abstract_integration_test_class import AbstractIntegrationTestClass


class MovieRestApiIntegrationTest(unittest.TestCase, AbstractIntegrationTestClass):

    @classmethod
    def setUpClass(cls) -> None:
        cls.setup()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down()

    def test_should_fetch_movie_by_title(self):
        # given
        title = "matrix"
        url = "/api/v1/fetch-by-title"

        # when
        response = self.client.get(f"{url}?title={title}")

        # then
        self.assertIsNotNone(response)

        movie = response.json()
        self.assertEqual(movie['title'], 'matrix')
        self.assertEqual(movie['director'], 'wachowski')
        self.assertEqual(movie['year'], 1999)
        self.assertEqual(movie['genre'], 'action')

    def test_should_raise_an_exception_if_movie_title_is_invalid(self):
        # given
        title = "matrix46"
        url = "/api/v1/fetch-by-title"

        # when
        with self.assertRaises(Exception) as context:
            self.client.get(f"{url}?title={title}")

        # then
        self.assertTrue('Title is invalid.' in str(context.exception))

    def test_should_not_fetch_movie_by_title_if_it_does_not_exist(self):
        # given
        title = "m"
        url = "/api/v1/fetch-by-title"

        # when
        response = self.client.get(f"{url}?title={title}")

        # then
        self.assertIsNotNone(response)

        movie = response.json()
        self.assertIsNone(movie)

    def test_should_fetch_all_movies(self):
        # given
        url = "/api/v1/fetch-all"

        # when
        response = self.client.get(f"{url}")

        # then
        self.assertIsNotNone(response)

        movie_list = response.json()
        self.assertEqual(len(movie_list), 3)

        self.assertEqual(movie_list[0]['title'], 'matrix')
        self.assertEqual(movie_list[0]['director'], 'wachowski')
        self.assertEqual(movie_list[0]['year'], 1999)
        self.assertEqual(movie_list[0]['genre'], 'action')

        self.assertEqual(movie_list[1]['title'], 'goodfellas')
        self.assertEqual(movie_list[1]['director'], 'scorsese')
        self.assertEqual(movie_list[1]['year'], 1990)
        self.assertEqual(movie_list[1]['genre'], 'biography')

        self.assertEqual(movie_list[2]['title'], 'se7en')
        self.assertEqual(movie_list[2]['director'], 'fincher')
        self.assertEqual(movie_list[2]['year'], 1995)
        self.assertEqual(movie_list[2]['genre'], 'crime')

    def test_should_save_movie(self):
        # given
        url = "/api/v1/save-movie"

        title = 'Superbad'
        director = 'Greg Mottola'
        year = 2007
        genre = 'comedy'

        data = {'title': title,
                'director': director,
                'year': year,
                'genre': genre}

        # when
        self.client.post(f"{url}", params=data)

        # then
        connection = self.create_connection()
        query = f"select * from test.movie where title = '{title}' " \
                f"and director = '{director}' " \
                f"and year = '{year}' " \
                f"and genre = '{genre}' "

        movie_fetched = pd.read_sql(query, con=connection)

        #self.assertEqual(len(movie_fetched), 1)
        self.assertEqual(movie_fetched.iloc[0]['title'], title)
        self.assertEqual(movie_fetched.iloc[0]['director'], director)
        self.assertEqual(movie_fetched.iloc[0]['year'], year)
        self.assertEqual(movie_fetched.iloc[0]['genre'], genre)