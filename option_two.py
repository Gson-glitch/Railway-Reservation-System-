import os
import tkinter
from tkinter import ttk, END
import customtkinter
import sqlite3
from database_utils import get_passengers_from_day


# ESTABLISHING A CONNECTION TO THE DATABASE
conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x400")
app.resizable(False, False)
app.title("OPTION #2 MENU")

# TEXT LABEL TITLE
text_title = tkinter.StringVar(value="Please enter a day:")
title_label = customtkinter.CTkLabel(master=app,
                                     textvariable=text_title,
                                     corner_radius=8)
title_label.place(relx=0.05, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 16))

# CREATING AN ENTRY WIDGET
choice_entry = customtkinter.CTkEntry(master=app,
                                      placeholder_text="Enter a day",
                                      width=420,
                                      height=25,
                                      border_width=2,
                                      corner_radius=10)
choice_entry.place(relx=0.05, rely=0.15, anchor=tkinter.W)


def submit_button_handler():
    res = get_passengers_from_day(choice_entry.get())

    # DAY LABEL
    day = customtkinter.CTkLabel(master=app)
    day.place(relx=0.05, rely=0.25, anchor=tkinter.W)
    day.configure(font=("Serif", 14))

    # HEADER LABEL
    header = customtkinter.CTkLabel(master=app)
    header.place(relx=0.05, rely=0.32, anchor=tkinter.W)
    header.configure(font=("Sans", 14))

    # CREATING A TEXT WIDGET
    text = tkinter.Text(app, height=10)
    text.configure(width=50)

    # create a scrollbar widget and set its command to the text widget
    scrollbar = ttk.Scrollbar(app, orient='vertical', command=text.yview)

    #  communicate back to the scrollbar
    text['yscrollcommand'] = scrollbar.set

    # print(res)
    if res:
        day.configure(text=f"Passengers travelling on {choice_entry.get().title()}:")
        header.configure(text="Passenger Name")

        text.place(x=30, y=160)
        scrollbar.place(x=420, y=160)

        for i in range(len(res)):
            position = f"{i+1}.0"
            text.insert(position, f"{res[i][0]}\n")

    else:
        day.configure(text=f"Invalid day {choice_entry.get()}{' '*100}")
        text.delete('1.0', END)
        header.configure(text=f"{' '*100}")


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
