import tkinter as tk
from tkinter import *

import os
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = tk.Tk()
root.title('Desktop Application')
root.geometry("300x400")


def login():
    con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
    cursor = con.cursor()

    # trying to check conditions with this
    #if e_eID.get() == cursor.execute("SELECT * FROM Employee WHERE eID='" + e_eID.get() + "'"):
    #    os.system("python3 main.py")
    #else:
    #    MessageBox.showinfo("Login Failed", "Enter valid login information")


    # works but doesnt check conditions
    if e_eID.get() == "" or e_name.get() == "":
        MessageBox.showinfo("Login Failed", "Enter valid login information")
    else:
        os.system("python3 ManagmentSystemDB/main.py")



# label inserts what the entry does in the program
eID = Label(root, text="Employee ID:", font=('bold',14))
eID.place(x=20, y=30)

name = Label(root, text="Name:", font=('bold', 14))
name.place(x=20, y=60)

#entry and placement for employee ID variable in database
e_eID = Entry()
e_eID.place(x=150, y=30)

#entry and placement for name variable in database
e_name = Entry()
e_name.place(x=150, y=60)

loginButton = Button(root, text="Login", command=login)
loginButton.place(x=130, y=100)

#executes employee gui table
openEmployee = Button(root, text='Employee Schedule', font=('italic', 30), bg="white", command=login)
openEmployee.place(x=10, y=400)

root.mainloop()
