from model.entity.ticket import Ticket
from model.business_logic.ticket_bl import TicketBl


class TicketController:

    def save (self ,  ticket_id , ticket_code , source , destination , airline , start_date_time , end_date_time , price , seat_no ,sold):
        try:
          ticket = Ticket( ticket_id , ticket_code , source , destination , airline , start_date_time , end_date_time , price , seat_no ,sold)
          ticket.validate()
          ticket_bl = TicketBl()
          TicketBl.save(ticket)

        except Exception as e:
            return f"Error:{str (e)}"





