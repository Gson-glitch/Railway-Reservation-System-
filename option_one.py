import os
import tkinter
import customtkinter
import sqlite3
from database_utils import get_train_from_full_names


# ESTABLISHING A CONNECTION TO THE DATABASE
conn = sqlite3.connect('rrs.db')
conn.execute("PRAGMA foreign_keys=ON")  # Enabling FOREIGN KEYS
cur = conn.cursor()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x400")
app.resizable(False, False)
app.title("OPTION #1 MENU")

# TEXT LABEL TITLE
text_title = tkinter.StringVar(value="Please enter the full names of the passenger:")
title_label = customtkinter.CTkLabel(master=app,
                                     textvariable=text_title,
                                     corner_radius=8)
title_label.place(relx=0.05, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 16))

# CREATING AN ENTRY WIDGET
choice_entry = customtkinter.CTkEntry(master=app,
                                      placeholder_text="Enter Passenger Full Names (FirstName LastName)",
                                      width=420,
                                      height=25,
                                      border_width=2,
                                      corner_radius=10)
choice_entry.place(relx=0.05, rely=0.15, anchor=tkinter.W)


def submit_button_handler():
    res = get_train_from_full_names(choice_entry.get())
    # PASSENGER NAME LABEL
    passenger_name = customtkinter.CTkLabel(master=app)
    passenger_name.place(relx=0.05, rely=0.25, anchor=tkinter.W)
    passenger_name.configure(font=("Serif", 14))

    # HEADER LABEL
    header = customtkinter.CTkLabel(master=app)
    header.place(relx=0.05, rely=0.32, anchor=tkinter.W)
    header.configure(font=("Sans", 14))

    # RESULTS LABELS
    x_axis = 35
    y_axis = 150
    res_labels = {}
    for data in res:
        res_labels[data[1]] = tkinter.Label(master=app)
        res_labels[data[1]].place(x=x_axis, y=y_axis)
        y_axis += 26

    # print(res)
    if res:
        passenger_name.configure(text=f"{choice_entry.get().title()} is booked on the following Train(s)")
        header.configure(text="Train Number\t\tTrain Name")

        for data in res:
            res_labels[data[1]].configure(text=f"{data[0]}\t\t\t{' ' * 5}{data[1]}")


        # x_axis = 35
        # y_axis = 150
        # for data in res:
        #     tkinter.Label(app, text=f"{data[0]}\t\t\t{' ' * 5}{data[1]}").place(x=x_axis, y=y_axis)
        #     y_axis += 26

    else:
        passenger_name.configure(text=f"{choice_entry.get()} isn't registered as a Passenger in the database.")
        header.configure(text=f"{' '*100}")
        print("UNKNOWN PERSON")


def back_button_handler():
    app.destroy()
    os.system('python3 gui.py')


# CREATING A BACK BUTTON
back_button = customtkinter.CTkButton(master=app, text="BACK TO MAIN MENU", command=back_button_handler)
back_button.place(relx=0.05, rely=0.80, anchor=tkinter.W)

# CREATING A SUBMIT BUTTON
submit_button = customtkinter.CTkButton(master=app, text="SUBMIT", command=submit_button_handler)
submit_button.place(relx=0.7, rely=0.80, anchor=tkinter.W)


app.mainloop()

conn.commit()
conn.close()
