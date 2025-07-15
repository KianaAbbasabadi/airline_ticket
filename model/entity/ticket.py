from model.tools.ticket_validation import *

class Ticket:
    def __init__(self , ticket_id , ticket_code , source , destination , airline , start_date_time , end_date_time , price , seat_no ,sold):
        self.ticket_id = ticket_id
        self.ticket_code = ticket_code
        self.source = source
        self.destination = destination
        self.airline = airline
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.price = price
        self.seat_no = seat_no
        self.sold = sold


    def to_tuple(self):
        return (self.ticket_id , self.ticket_code , self.source , self.destination ,self.airline , self.start_date_time , self.end_date_time , self.price , self.seat_no , self.sold )


    def validate(self):
        validation=Validation()
        return validation.ticket_validator(self)


