from tkinter import *
from controller.user_controller  import UserController
from view import *
import tkinter.messagebox as msg


class UserView:
    def save_click(self):
        user_controller = UserController()
        status, message = user_controller.save(
            self.id.get(),
            self.name.get(),
            self.family.get(),
            self.birthdate.get(),
            self.username.get(),
            self.password.get(),
            self.role.get()

        )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)


    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x300")

        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birthdate = IntVar()
        self.username = StringVar()
        self.password = IntVar()
        self.role = StringVar()

        Entry(self.win, textvariable=self.id).pack()
        Entry(self.win, textvariable=self.name).pack()
        Entry(self.win, textvariable=self.family).pack()
        Entry(self.win, textvariable=self.birthdate).pack()
        Entry(self.win, textvariable=self.username).pack()
        Entry(self.win, textvariable=self.role).pack()


        Button(self.win, text="Save", command=self.save_click).pack()
