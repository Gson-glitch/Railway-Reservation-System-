import os
import tkinter
from tkinter import ttk
import customtkinter
import sqlite3
from database_utils import get_train_info_and_passenger_info_from_age


# ESTABLISHING A CONNECTION TO THE DATABASE
conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1260x400")
app.resizable(False, False)
app.title("OPTION #3 MENU")

# TEXT LABEL TITLE
text_title = tkinter.StringVar(value="Please enter the age of a passenger (50-60):")
title_label = customtkinter.CTkLabel(master=app,
                                     textvariable=text_title,
                                     corner_radius=8)
title_label.place(relx=0.05, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 16))

# CREATING AN ENTRY WIDGET
choice_entry = customtkinter.CTkEntry(master=app,
                                      placeholder_text="Enter age",
                                      width=420,
                                      height=25,
                                      border_width=2,
                                      corner_radius=10)
choice_entry.place(relx=0.05, rely=0.15, anchor=tkinter.W)


def submit_button_handler():
    age = -1
    try:
        age = int(choice_entry.get())
    except ValueError:
        return
    res = get_train_info_and_passenger_info_from_age(age)

    # AGE LABEL
    day = customtkinter.CTkLabel(master=app)
    day.place(relx=0.05, rely=0.25, anchor=tkinter.W)
    day.configure(font=("Serif", 14))

    # HEADER LABEL
    header = customtkinter.CTkLabel(master=app)
    header.place(relx=0.025, rely=0.32, anchor=tkinter.W)
    header.configure(font=("Sans", 14))

    # CREATING A TEXT WIDGET
    text = tkinter.Text(app, height=10)
    text.configure(width=150)

    # create a scrollbar widget and set its command to the text widget
    scrollbar = ttk.Scrollbar(app, orient='vertical', command=text.yview)

    #  communicate back to the scrollbar
    text['yscrollcommand'] = scrollbar.set

    for data in res:
        print(data)

    # print(res)
    if res:
        day.configure(text="Passenger's Details and Train Information")
        header.configure(text=f"Passenger Name\t{' '*13}Address\t\t{' '*7}Ticket Type\t{' '*2}Status\t{' '*16}Train Number{' '*7}Train Name\t{' '*16}Source\t{' '*13}Destination")

        text.place(x=30, y=160)
        scrollbar.place(x=1220, y=160)

        for i in range(len(res)):
            position = f"{i+1}.0"
            # text.insert(position, f"{res[i][0]}  {res[i][1]}  {res[i][2]}   {res[i][3]}  {res[i][4]}  {res[i][5]}  {res[i][6]}  {res[i][7]}\n")
            text.insert(position, f"{res[i][0]}\t\t\t{res[i][1]}\t\t\t{res[i][2]}\t\t{res[i][3]}\t\t{res[i][4]}\t\t{res[i][5]}\t\t{' '*4}{res[i][6]}\t\t{' '*5}{res[i][7]}\n")

    else:
        day.configure(text=f"Invalid day {choice_entry.get()}")


def back_button_handler():
    app.destroy()
    os.system('python3 gui.py')


# CREATING A BACK BUTTON
back_button = customtkinter.CTkButton(master=app, text="BACK TO MAIN MENU", command=back_button_handler)
back_button.place(relx=0.05, rely=0.93, anchor=tkinter.W)

# CREATING A SUBMIT BUTTON
submit_button = customtkinter.CTkButton(master=app, text="SUBMIT", command=submit_button_handler)
submit_button.place(relx=0.7, rely=0.93, anchor=tkinter.W)


app.mainloop()

conn.commit()
conn.close()
