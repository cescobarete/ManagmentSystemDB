import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def update():

    eID = d_eID.get()
    pID = d_pID.get()
    yearlySalary = d_yearlySalary.get()
    email = d_email.get()
    review = d_review.get()

    if (eID=="" or pID=="" or yearlySalary=="" or email=="" or review==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("UPDATE PersonalInfo SET yearlySalary='"+yearlySalary+"', email='"+email+"', review='"+review+"' WHERE eID='"+eID+"' AND pID='"+pID+"'")
        cursor.execute("commit")

        d_eID.delete(0, 'end')
        d_pID.delete(0, 'end')
        d_yearlySalary.delete(0, 'end')
        d_email.delete(0, 'end')
        d_review.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def get():
    if (d_eID.get() == "" and d_pID.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID fields required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM PersonalInfo WHERE eID='"+d_eID.get()+"' AND pID='"+d_pID.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            d_yearlySalary.insert(0, row[2])
            d_email.insert(0, row[3])
            d_review.insert(0, row[4])

        con.close()

root = Tk()
root.geometry("700x500")
root.title("Managment System: Personal Info")

eID = Label(root, text="Enter employee ID:", font=('bold',14))
eID.place(x=20, y=30)

pID = Label(root, text="Enter position ID:", font=('bold',14))
pID.place(x=20, y=60)

yearlySalary = Label(root, text="Salary:", font=('bold',14))
yearlySalary.place(x=20, y=90)

email = Label(root, text="Email:", font=('bold',14))
email.place(x=20, y=120)

review = Label(root, text="Review:", font=('bold',14))
review.place(x=20, y=150)

d_eID = Entry()
d_eID.place(x=150, y=30)

d_pID = Entry()
d_pID.place(x=150, y=60)

d_yearlySalary = Entry()
d_yearlySalary.place(x=150, y=90)

d_email = Entry()
d_email.place(x=150, y=120)

d_review = Entry()
d_review.place(x=150, y=150)

update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=20, y=190)

get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=100, y=190)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

trev = ttk.Treeview(columns=(1,2,3,4,5,6), show="headings", height="13")
trev.place(x=10, y=220)

trev.heading(1, text="Name")
trev.heading(2, text="Employee ID")
trev.heading(3, text="Position ID")
trev.heading(4, text="Salary")
trev.heading(5, text="E-mail")
trev.heading(6, text="Review")

sql = "SELECT name, PersonalInfo.eID, PersonalInfo.pID, yearlySalary, email, review FROM Company, Employee, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID ORDER BY PersonalInfo.eID ASC"
cursor.execute(sql)
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

root.mainloop()