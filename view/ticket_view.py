from optparse import Values
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


city=["Tehran" , "Mashhad " , "Rasht" , "kish" , "Esfahan" , "birjand" , "Qeshm"]
airlines=["Mahan air" , "Homa air" , "Aseman air" , "Kish air" , "iran air"]

def reset_form(self):
   self.id_ticket.set(0)
   self.source_ticket("")
   self.destination_ticket("")
   self.seat_ticket("")
   self.start_date("")
   self.end_date("")
   self.airline()



class TicketView:
    def save_btn_click(self):
     ticket = (self.id_ticket.get() , self.source_ticket.get(), self.destination_ticket.get() , )

    def edit_btn_click(self):
        pass

    def remove_btn_click(self):
        pass

    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title('Ticket')

        # ID
        Label(self.window, text="ID").place(x=10, y=20)
        self.id_ticket = IntVar()
        Entry(self.window, textvariable=self.id_ticket).place(x=100, y=20)

        # source
        Label(self.window, text="Source").place(x=10, y=50)
        self.source_ticket = StringVar(value="Tehran")
        ttk.Combobox(self.window, textvariable=self.source_ticket, values=city, state="readonly").place(x=100, y=50)

        # destination
        Label(self.window, text="Destination").place(x=10, y=80)
        self.destination_ticket = StringVar(value="Mashhad ")
        ttk.Combobox(self.window, textvariable=self.destination_ticket, values=city, state="readonly").place(x=100, y=80)

        # seat number
        Label(self.window, text="seat number").place(x=10, y=120)
        self.seat_ticket = IntVar()
        Entry(self.window, textvariable=self.seat_ticket).place(x=100, y=120)
        # start date time
        Label(self.window, text="start date time").place(x=10, y=160)
        self.start_date = StringVar()
        Entry(self.window, textvariable=self.start_date).place(x=100, y=160)

        # end date time
        Label(self.window, text="end date time").place(x=10, y=190)
        self.end_date = StringVar()
        Entry(self.window, textvariable=self.end_date).place(x=100, y=190)

        # airline
        Label(self.window, text="Airline").place(x=10, y=230)
        self.airline = StringVar()
        ttk.Combobox(self.window, textvariable=self.airline, values=airlines, state="readonly").place(x=100, y=230)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")
        self.table.heading(1 , text="ID")
        self.table.heading(2 , text="Source")
        self.table.heading(3 , text="Destination")
        self.table.heading(4 , text="seat number")
        self.table.heading(5 , text="start date time")
        self.table.heading(6 , text="end date time")
        self.table.heading(7 , text="Airline")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)

        self.table.place(x=300 , y=20)


        Button(self.window, text="Save", command=self.save_btn_click).place(x=10, y=300)
        Button(self.window, text="Edit", command=self.edit_btn_click).place(x=100, y=300)
        Button(self.window, text="Remove", command=self.remove_btn_click).place(x=200, y=300)

        self.window.mainloop()