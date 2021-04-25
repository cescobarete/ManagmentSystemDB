import tkinter as tk
from tkinter import *
from tkinter import ttk

import os

import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = tk.Tk()
root.title('Employee Login')
root.geometry("400x300")
#keep window from resizing 
root.resizable(False,False)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#def tree():
    #database displaying information within gui
#    trev2 = ttk.Treeview(root,columns=(1), show="headings", height="1")

    #headings for each piece of info displayed
#    trev2.heading(1, text="Days Employee Works")

    #select for info being grabbed from database
#    cursor.execute("SELECT COUNT mon, tue, wed, thur, fri, sat, sun FROM Employee WHERE mon = 'Y' or tue = 'Y' or wed = 'Y' or thur = 'Y' or sat = 'Y' or sun = 'Y'")
#    rows = cursor.fetchall()

#    for i in rows:
#        trev2.insert('','end',values=i)

#    trev2.pack()

def user_login(tup):
    try:
        cursor.execute("SELECT Employee.eID, Company.pswd, Company.privilege FROM Employee INNER JOIN PersonalInfo ON Employee.eID = PersonalInfo.eID INNER JOIN Company ON PersonalInfo.pID = Company.pID WHERE Employee.eID = '"+e_eID.get()+"' AND Company.pswd = '"+e_pswd.get()+"'")
        return(cursor.fetchone())
    except:
        return False

#test user data to see if they can log in
def login():
    data = {
        e_eID.get(),
        e_pswd.get()
    }
    
    if e_eID.get() == "" or e_pswd.get() == "":
        MessageBox.showinfo("Login Failed", "Enter both username/password")
    else:
        #grabs data from user login that gets the data with a select statement
        res = user_login(data)
        if res:
            MessageBox.showinfo("Login", "Login Successful")
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()

            root = Tk()
            root.geometry("1000x500")
            root.title("User Information")

            #tree()

            #database displaying information within gui
            trev = ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), show="headings", height="1")

            #headings for each piece of info displayed
            trev.heading(1, text="Name")
            trev.heading(2, text="Employee ID")
            trev.heading(3, text="Start Time")
            trev.heading(4, text="End Time")
            trev.heading(5, text="Position ID")
            trev.heading(6, text="Position")
            trev.heading(7, text="Salary")
            trev.heading(8, text="E-mail")
            trev.heading(9, text="Schedule Creation")
            trev.heading(10, text="Monday")
            trev.heading(11, text="Tuesday")
            trev.heading(12, text="Wednesday")
            trev.heading(13, text="Thursday")
            trev.heading(14, text="Friday")
            trev.heading(15, text="Saturday")
            trev.heading(16, text="Sunday")


            #select for info being grabbed from database
            cursor.execute("SELECT name, Employee.eID, startTime, endTime, Company.pID, position, yearlySalary, email, mon, tue, wed, thur, fri, sat, sun FROM Employee INNER JOIN PersonalInfo ON Employee.eID = PersonalInfo.eID INNER JOIN Company ON PersonalInfo.pID = Company.pID WHERE Employee.eID = '"+e_eID.get()+"' AND Company.pswd = '"+e_pswd.get()+"'")
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

pswd = Label(root, text="Password:", font=('bold', 14))
pswd.place(x=20, y=60)

#entry and placement for employee ID variable in database
e_eID = Entry()
e_eID.place(x=150, y=30)

e_pswd = Entry(show='*')
e_pswd.place(x=150, y=60)

loginButton = Button(root, text="Login", command=login)
loginButton.place(x=20, y=100)

root.mainloop()
