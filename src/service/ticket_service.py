class TicketService:

    def define_ticket_price(self, movie: str) -> int:
        if len(movie) > 5:
            return 10
        else:
            return 20