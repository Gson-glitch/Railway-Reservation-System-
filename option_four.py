import os
import tkinter
from tkinter import ttk
import customtkinter
import sqlite3
from database_utils import get_train_status


# ESTABLISHING A CONNECTION TO THE DATABASE
conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")
app.resizable(False, False)
app.title("OPTION #4 MENU")

# TEXT LABEL TITLE
text_title = tkinter.StringVar(value="Count of Passengers in Each Train")
title_label = customtkinter.CTkLabel(master=app,
                                     textvariable=text_title,
                                     corner_radius=8)
title_label.place(relx=0.05, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 16))

res = get_train_status()

# COUNT OF PASSENGERS LABEL
count_of_passengers_label = customtkinter.CTkLabel(master=app)
count_of_passengers_label.place(relx=0.05, rely=0.25, anchor=tkinter.W)
count_of_passengers_label.configure(font=("Serif", 14))
count_of_passengers_label.configure(text=f"Train Status")

# HEADER LABEL
header = customtkinter.CTkLabel(master=app)
header.place(relx=0.05, rely=0.32, anchor=tkinter.W)
header.configure(font=("Sans", 14))
header.configure(text="Train Name\t\t\tCount of Passengers")

# CREATING A TEXT WIDGET
text = tkinter.Text(app, height=10)
text.configure(width=53)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(app, orient='vertical', command=text.yview)
scrollbar.place(x=444, y=160)

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set
text.place(x=30, y=160)

for i in range(len(res)):
    position = f"{i+1}.0"
    text.insert(position, f"{res[i][0]}\t\t\t\t\t\t{res[i][1]}\n")


def back_button_handler():
    app.destroy()
    os.system('python3 gui.py')


# CREATING A BACK BUTTON
back_button = customtkinter.CTkButton(master=app, text="BACK TO MAIN MENU", command=back_button_handler)
back_button.place(relx=0.35, rely=0.93, anchor=tkinter.W)


app.mainloop()

conn.commit()
conn.close()
