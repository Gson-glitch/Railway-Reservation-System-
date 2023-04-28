import os
import tkinter
from tkinter import ttk, END
import customtkinter
import sqlite3
from database_utils import get_passengers_with_confirmed_tickets, cancel_ticket


# ESTABLISHING A CONNECTION TO THE DATABASE
conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")
app.resizable(False, False)
app.title("OPTION #6 MENU")

# TEXT LABEL TITLE
text_title = tkinter.StringVar(value="Passengers with Confirmed Tickets")
title_label = customtkinter.CTkLabel(master=app,
                                     textvariable=text_title,
                                     corner_radius=8)
title_label.place(relx=0.035, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 16))

res = get_passengers_with_confirmed_tickets()

# HEADER LABEL
header = customtkinter.CTkLabel(master=app)
header.place(relx=0.05, rely=0.1, anchor=tkinter.W)
header.configure(font=("Sans", 14))
header.configure(text="Passenger Name")

# CREATING A TEXT WIDGET
text = tkinter.Text(app, height=10)
text.configure(width=53)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(app, orient='vertical', command=text.yview)
scrollbar.place(x=444, y=60)

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set
text.place(x=30, y=60)

for i in range(len(res)):
    position = f"{i+1}.0"
    text.insert(position, f"{res[i][0]}\n")


# PASSENGER TO CANCEL LABEL
passenger_to_cancel_label = customtkinter.CTkLabel(master=app)
passenger_to_cancel_label.place(relx=0.05, rely=0.65, anchor=tkinter.W)
passenger_to_cancel_label.configure(font=("Sans", 14))
passenger_to_cancel_label.configure(text="Passenger Name to Cancel Order: ")

# PASSENGER TO CANCEL ENTRY
passenger_to_cancel_entry = customtkinter.CTkEntry(master=app,
                                      placeholder_text="Enter Passenger Name",
                                      width=174,
                                      height=25,
                                      border_width=2,
                                      corner_radius=10)
passenger_to_cancel_entry.place(relx=0.57, rely=0.65, anchor=tkinter.W)


def cancel_ticket_handler():
    cancel_ticket(passenger_to_cancel_entry.get())
    updated_records = get_passengers_with_confirmed_tickets()
    # print(updated_records)
    text.delete('1.0', END)
    for i in range(len(updated_records)):
        override_position = f"{i+1}.0"
        text.insert(override_position, f"{updated_records[i][0]}\n")
    text.update()


# CREATING A CANCEL TICKET BUTTON
cancel_ticket_button = customtkinter.CTkButton(master=app, text="CANCEL TICKET", command=cancel_ticket_handler)
cancel_ticket_button.place(relx=0.35, rely=0.83, anchor=tkinter.W)


def back_button_handler():
    app.destroy()
    os.system('python3 gui.py')


# CREATING A BACK BUTTON
back_button = customtkinter.CTkButton(master=app, text="BACK TO MAIN MENU", command=back_button_handler)
back_button.place(relx=0.35, rely=0.93, anchor=tkinter.W)


app.mainloop()

conn.commit()
conn.close()
