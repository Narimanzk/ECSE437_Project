from src.service.organization_service import OrganizationService
from src.service.ticket_service import TicketService


class ShowService:

    def __init__(self):
        self.__organization_service = OrganizationService()
        self.__ticket_service = TicketService()

    def organize_show(self):
        show: str = self.__organization_service.choose_show()
        ticket_price: int = self.__ticket_service.define_ticket_price(show)
        return {'show': show,
                'ticket_price': ticket_price}