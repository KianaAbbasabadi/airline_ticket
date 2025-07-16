from datetime import datetime, timedelta
from model.entity.ticket import *
from model.data_access.ticket_da import TicketDa


class TicketBl:
    def save(self, ticket):
        time_now = datetime.now()
        min_start_time = time_now + timedelta(hours=5)

        if Ticket.start_date_time < min_start_time:
            raise ValueError('Start date time must be at least 5 hours from now !!!')

    def edited(self, ticket):
        print("Ticket edited from db", ticket.ticket_code)

    def remove(self, ticket):
        print("Ticket remove from db", ticket)

    def find_by_ticket_code(self, ticket_code):
        pass

    def find_by_source(self, source):
        pass

    def find_by_destination(self, destination):
        pass

    def find_by_airline(self, airline):
        pass

    def find_by_start_date_time(self, start_date_time):
        pass

    def find_by_end_date_time(self, end_date_time):
        pass

    def find_by_sold(self, sold):
        pass