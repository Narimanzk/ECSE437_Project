from src.service.organization_service import OrganizationService
from src.service.ticket_service import TicketService


class ConcertService:

    def __init__(self):
        self.__organization_service = OrganizationService()
        self.__ticket_service = TicketService()

    def organize_show(self):
        movie: str = self.__organization_service.choose_movie()
        ticket_price: int = self.__ticket_service.define_ticket_price(movie)
        return {'movie': movie,
                'ticket_price': ticket_price}