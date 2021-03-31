import tkinter as tk
from tkinter import *
from tkinter import ttk

import os

import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = tk.Tk()
root.title('Employee Login')
root.geometry("400x300")
root.resizable(False,False)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

def user_login(tup):
    try:
        cursor.execute("SELECT * FROM Employee WHERE eID='"+e_eID.get()+"' AND name='"+e_name.get()+"'")
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
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()

            root = Tk()
            root.geometry("1000x500")
            root.title("User Information")

            #database displaying information within gui
            trev = ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9), show="headings", height="1")

            #headings for each piece of info displayed
            trev.heading(1, text="Name")
            trev.heading(2, text="Employee ID")
            trev.heading(3, text="Start Time")
            trev.heading(4, text="End Time")
            trev.heading(5, text="Position ID")
            trev.heading(6, text="Position")
            trev.heading(7, text="Salary")
            trev.heading(8, text="E-mail")
            trev.heading(9, text="Directive")

            #select for info being grabbed from database
            cursor.execute("SELECT name, Employee.eID, startTime, endTime, Company.pID, position, yearlySalary, email, directive FROM Employee INNER JOIN PersonalInfo ON Employee.eID = PersonalInfo.eID INNER JOIN Company ON PersonalInfo.pID = Company.pID WHERE Employee.eID = '"+e_eID.get()+"' AND Employee.name = '"+e_name.get()+"'")
            rows = cursor.fetchall()

            for i in rows:
                trev.insert('','end',values=i)

            hsb = ttk.Scrollbar(root,orient="horizontal")
            hsb.configure(command=trev.xview)
            trev.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X,side=BOTTOM)

            trev.pack()
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

loginButton = Button(root, text="Login", command=login)
loginButton.place(x=20, y=100)

root.mainloop()
