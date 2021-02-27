import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

con = mysql.connector.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

sql = "SELECT * FROM Employee"
cursor.execute(sql)
rows = cursor.fetchall()

root = Tk()

frm = Frame(root)
frm.pack(side=tk.LEFT, padx=20)

tv = ttk.Treeview(frm, column=(1,2,3,4), show="headings", height="5")
tv.pack()

tv.heading(1, text="Employee ID")
tv.heading(2, text="Name")
tv.heading(3, text="Start Time")
tv.heading(4, text="End Time")

for i in rows:
    tv.insert('','end',values=i)

root.title('Employee Data')
root.geometry("900x500")
root.resizable(False,False)
root.mainloop()