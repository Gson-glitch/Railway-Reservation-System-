import tkinter
import customtkinter
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x400")
app.resizable(False, False)
app.title("RRS GUI")


def button_function():
    user_choice = -1
    try:
        user_choice = int(choice_entry.get())
    except ValueError:
        pass

    if user_choice == 1:
        app.destroy()
        os.system("python3 option_one.py")
    elif user_choice == 2:
        app.destroy()
        os.system("python3 option_two.py")
    elif user_choice == 3:
        app.destroy()
        os.system("python3 option_three.py")
    elif user_choice == 4:
        app.destroy()
        os.system("python3 option_four.py")
    elif user_choice == 5:
        app.destroy()
        os.system("python3 option_five.py")
    elif user_choice == 6:
        app.destroy()
        os.system("python3 option_six.py")
    # print("button pressed")
    # print(choice_entry.get())
    # app.destroy()
    # os.system('python3 gui.py')


# CREATING A LABEL WIDGET
# TEXT TITLE LABEL
text_title = tkinter.StringVar(value="Please Select an Option from the List Below:")
title_label = customtkinter.CTkLabel(master=app,
                               textvariable=text_title,
                               corner_radius=8)
title_label.place(relx=0.05, rely=0.05, anchor=tkinter.W)
title_label.configure(font=("Courier", 20))

# OPTION ONE LABEL
option_one_label = customtkinter.CTkLabel(master=app, text="1. Retrieve all trains a passenger is booked on.")
option_one_label.place(relx=0.16, rely=0.21, anchor=tkinter.W)
option_one_label.configure(font=("Sans", 16))

# OPTION TWO LABEL
option_two_label = customtkinter.CTkLabel(master=app, text="2. Retrieve passengers travelling on a particular day.")
option_two_label.place(relx=0.16, rely=0.27, anchor=tkinter.W)
option_two_label.configure(font=("Sans", 16))

# OPTION THREE LABEL
option_three_label = customtkinter.CTkLabel(master=app, text="3. Display train and passenger info from age (50-60).")
option_three_label.place(relx=0.16, rely=0.33, anchor=tkinter.W)
option_three_label.configure(font=("Sans", 16))

# OPTION FOUR LABEL
option_four_label = customtkinter.CTkLabel(master=app, text="4. List the count of passengers in each train.")
option_four_label.place(relx=0.16, rely=0.39, anchor=tkinter.W)
option_four_label.configure(font=("Sans", 16))

# OPTION FIVE LABEL
option_five_label = customtkinter.CTkLabel(master=app, text="5. Retrieve all passengers travelling on a particular train.")
option_five_label.place(relx=0.16, rely=0.45, anchor=tkinter.W)
option_five_label.configure(font=("Sans", 16))

# OPTION SIX LABEL
option_six_label = customtkinter.CTkLabel(master=app, text="6. Cancel a ticket for a particular user.")
option_six_label.place(relx=0.16, rely=0.51, anchor=tkinter.W)
option_six_label.configure(font=("Sans", 16))

# USER'S CHOICE
choice_text = tkinter.StringVar(value="Choice:")
user_choice_label = customtkinter.CTkLabel(master=app,
                                     textvariable=choice_text,
                                     corner_radius=8)
user_choice_label.place(relx=0.05, rely=0.67, anchor=tkinter.W)
user_choice_label.configure(font=("Courier", 20))

# CREATING AN ENTRY WIDGET
choice_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Please Select an Option Number",
                               width=420,
                               height=25,
                               border_width=2,
                               corner_radius=10)
choice_entry.place(relx=0.58, rely=0.67, anchor=tkinter.CENTER)

# CREATING A SUBMIT BUTTON
button = customtkinter.CTkButton(master=app, text="SUBMIT", command=button_function)
button.place(relx=0.4, rely=0.80, anchor=tkinter.W)


def close_app():
    app.destroy()


# CREATING AN EXIT BUTTON
exit_button = customtkinter.CTkButton(master=app, text="EXIT", command=close_app)
exit_button.place(relx=0.4, rely=0.90, anchor=tkinter.W)

app.mainloop()
