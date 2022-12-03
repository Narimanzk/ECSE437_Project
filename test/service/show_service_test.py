import unittest
from unittest.mock import patch

from src.service.show_service import ShowService


class ShowServiceTest(unittest.TestCase):

    def test_should_organize_show_with_default_values(self):
        # given
        show_service = ShowService()

        # when
        show_details = show_service.organize_show()

        # then
        self.assertIsNotNone(show_details)
        self.assertEqual(show_details['show'], 'Avatar')
        self.assertEqual(show_details['ticket_price'], 10)

    @patch("src.service.ticket_service.TicketService.define_ticket_price")
    @patch("src.service.organization_service.OrganizationService.choose_show")
    def test_should_organize_show_with_mocked_values(self,
                                                        mock_choose_show,
                                                        mock_define_ticket_price):
        # given
        show_service = ShowService()

        mock_choose_show.return_value = "Parasite"
        mock_define_ticket_price.return_value = 100

        # when
        show_details = show_service.organize_show()

        # then
        self.assertIsNotNone(show_details)
        self.assertEqual(show_details['show'], 'Parasite')
        self.assertEqual(show_details['ticket_price'], 100)