import unittest

from src.validation.movie_validation_service import MovieValidationService


class MovieValidationServiceTest(unittest.TestCase):

    def test_should_raise_an_exception_when_title_is_invalid(self):
        # given
        title = 'matrics8'

        # when
        with self.assertRaises(Exception) as context:
            MovieValidationService.validate_title(title)

        # then
        self.assertTrue('Title is invalid.' in str(context.exception))

    def test_should_not_raise_an_exception_when_title_is_valid(self):
        # given
        title = 'matrix'

        # when
        MovieValidationService.validate_title(title)