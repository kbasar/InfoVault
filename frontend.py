from tkinter import *
from backend import Database

database = Database("vault.db")


class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Information vault")

        l1 = Label(window, text="Item Description")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Link")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Username")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="Password")
        l4.grid(row=1, column=2)

        l5 = Label(window, text="Notes")
        l5.grid(row=0, column=5)

        self.desc_txt = StringVar()
        self.e1 = Entry(window, textvariable=self.desc_txt)
        self.e1.grid(row=0, column=1)

        self.link_txt = StringVar()
        self.e2 = Entry(window, textvariable=self.link_txt)
        self.e2.grid(row=0, column=3, columnspan=2)

        self.username_txt = StringVar()
        self.e3 = Entry(window, textvariable=self.username_txt)
        self.e3.grid(row=1, column=1)

        self.pass_txt = StringVar()
        self.e4 = Entry(window, textvariable=self.pass_txt)
        self.e4.grid(row=1, column=3)

        self.note_txt = StringVar()
        self.e5 = Entry(window, textvariable=self.note_txt)
        self.e5.grid(row=1, column=6, columnspan=10)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=3, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=3, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=3, column=3)

        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=4, column=3)

        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=5, column=3)

        b4 = Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=6, column=3)

        b5 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=7, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=8, column=3)

    def get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])
        self.e5.delete(0, END)
        self.e5.insert(END, self.selected_tuple[5])

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.desc_txt.get(), self.link_txt.get(), self.username_txt.get(), self.pass_txt.get(), self.note_txt.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.desc_txt.get(), self.link_txt.get(), self.username_txt.get(), self.pass_txt.get(), self.note_txt.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.desc_txt.get(), self.link_txt.get(), self.username_txt.get(), self.pass_txt.get(), self.note_txt.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.desc_txt.get(), self.link_txt.get(), self.username_txt.get(), self.pass_txt.get(), self.note_txt.get())


window = Tk()
Window(window)
window.mainloop()
