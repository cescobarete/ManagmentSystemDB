import tkinter as tk
from tkinter import *

import os

import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = tk.Tk()
root.title('Management Login System')
root.geometry("400x300")
root.resizable(False,False)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

def user_login(tup):
    try:
        cursor.execute("SELECT Employee.eID, Employee.name, Company.privilege FROM Employee INNER JOIN PersonalInfo ON Employee.eID = PersonalInfo.eID INNER JOIN Company ON PersonalInfo.pID = Company.pID WHERE Employee.eID = '"+e_eID.get()+"' AND Employee.name = '"+e_name.get()+"' AND Company.privilege = 'granted'")
        return(cursor.fetchone())
    except:
        return False

def login():

    data = {
        e_eID.get(),
        e_name.get()
    }

    if e_eID.get() == "" or e_name.get() == "":
        MessageBox.showinfo("Login Failed", "Enter both username/password")
    else:
        res = user_login(data)
        if res:
            MessageBox.showinfo("Login", "Login Successful")
            os.system("python3 manage-data.py")
        else:
            MessageBox.showinfo("Alert", "Wrong username/password")


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

e_priv = Entry()

loginButton = Button(root, text="Login", command=login)
loginButton.place(x=20, y=100)

root.mainloop()
