class TicketDa:
    def save(self , ticket):
        print("Ticket save to db" , ticket.ticket_code)

    def edited(self , ticket):
        print("Ticket edited from db" , ticket.ticket_code)


    def remove(self , ticket):
        print("Ticket remove from db" , ticket)

    def find_by_ticket_code(self , ticket_code):
        pass

    def find_by_source(self , source):
        pass

    def find_by_destination(self , destination):
        pass

    def find_by_airline(self , airline):
        pass

    def find_by_start_date_time(self , start_date_time):
        pass

    def find_by_end_date_time(self , end_date_time):
        pass


    def find_by_sold(self , sold):
        pass