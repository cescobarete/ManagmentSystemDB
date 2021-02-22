import tkinter as tk
from tkinter import *


master = tk.Tk()
master.title('Desktop Application')
master.geometry("300x400")


class Username:
    usernameLabel = Label(master, text="username").grid(row=1, column=0)
    usernameTextbox = tk.StringVar()
    nameEntered = Entry(master, width=30, textvariable=usernameTextbox).grid(row=1, column=1)


class Password:
    passwordLabel = Label(master, text="password").grid(row=2, column=0)
    passwordTextbox = tk.StringVar()
    passwordEntered = Entry(master, show="*", textvariable=passwordTextbox, width=30).grid(row=2, column=1)


def login():
    print(Username.usernameTextbox.get() + Password.passwordTextbox.get())


passwordCheckbox = IntVar()


def reveal():
    if passwordCheckbox.get() == 1:
        Password.passwordEntered = Entry(master, text=Password.passwordTextbox.get(), width=30).grid(row=2, column=1)

    elif passwordCheckbox.get() == 0:
        Password.passwordEntered = Entry(master, text=Password.passwordTextbox.get(), show="*", width=30).\
            grid(row=2, column=1)


checkButton = Checkbutton(master, text="show password", variable=passwordCheckbox, onvalue=1, offvalue=0,
                          command=reveal).grid(column=1)
loginButton = Button(master, text="Login", command=login).grid(column=1, pady=4)


master.mainloop()
