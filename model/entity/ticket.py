class Ticket:
    def __init__(self, code, source, destination, seat_ticket, start_date_time, end_date_time, airline):
        self.code = code
        self.source = source
        self.destination = destination
        self.seat_ticket = seat_ticket
        self.start_date = start_date
        self.end_date = end_date
        self.airline = airline

    def to_tuple(self):
        return tuple(self.__dict__.values())

    def __repr__(self):
        return f"{self.__dict__}"
