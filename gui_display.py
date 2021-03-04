import tkinter 
from tkinter import *
from tkinter import ttk

import mysql.connector

con = mysql.connector.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

sql = "SELECT Employee.eID, name, startTime, endTime, Company.pID, position, yearlySalary, email FROM Employee, Company, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID ORDER BY eID ASC"
cursor.execute(sql)
rows = cursor.fetchall()

root = Tk()

frm = Frame(root)
frm.pack(side=LEFT, padx=30)

tv = ttk.Treeview(frm, column=(1,2,3,4,5,6,7,8), show="headings", height="45")
tv.pack()

tv.heading(1, text="Employee ID")
tv.heading(2, text="Name")
tv.heading(3, text="Start Time")
tv.heading(4, text="End Time")
tv.heading(5, text="Position ID")
tv.heading(6, text="Position")
tv.heading(7, text="Salary")
tv.heading(8, text="E-mail")

for i in rows:
    tv.insert('','end',values=i)

root.title('Employee Data')
root.geometry("900x900")
root.resizable(False,False)
root.mainloop()