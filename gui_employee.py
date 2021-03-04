import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def insert():
    eID = e_eID.get()
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()

    if (eID=="" or name=="" or startTime=="" or endTime==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Employee VALUES('"+eID+"','"+name+"','"+startTime+"','"+endTime+"')")
        cursor.execute("commit")

        e_eID.delete(0, 'end')
        e_name.delete(0, 'end')
        e_startTime.delete(0, 'end')
        e_endTime.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()
    
def delete():
    if(e_eID.get() == ''):
        MessageBox.showinfo("Delete status","Deleted")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("DELETE FROM Employee WHERE eID='"+e_eID.get()+"'")
        cursor.execute("commit")

        e_eID.delete(0, 'end')
        e_name.delete(0, 'end')
        e_startTime.delete(0, 'end')
        e_endTime.delete(0, 'end')
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def update():
    #grabs information
    eID = e_eID.get()
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()
    pID = e_pID.get()

    #needs all fields to be filled or dont execute
    if (eID=="" or name=="" or startTime=="" or endTime=="" or pID==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("UPDATE Employee SET name='"+name+"', startTime='"+startTime+"', endTime='"+endTime+"' WHERE eID='"+eID+"'")
        cursor.execute("commit")
        cursor.execute("UPDATE Company SET pID='"+pID+"' WHERE pID='"+pID+"'")
        cursor.execute("commit")

        #if duplicate dont update
        e_eID.delete(0, 'end')
        e_name.delete(0, 'end')
        e_startTime.delete(0, 'end')
        e_endTime.delete(0, 'end')
        e_pID.delete(0, 'end')

        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def get():
    if (e_eID.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Employee WHERE eID='"+e_eID.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_startTime.insert(0, row[2])
            e_endTime.insert(0, row[3])

        con.close()

root = Tk()

root.geometry("700x500")
root.title("Managment System: Employee")

#label inserts what the entry does in the program
eID = Label(root, text="Employee ID:", font=('bold',14))
eID.place(x=20, y=30)

name = Label(root, text="Name:", font=('bold',14))
name.place(x=20, y=60)

startTime = Label(root, text="Start time:", font=('bold',14))
startTime.place(x=20, y=90)

endTime = Label(root, text="End time:", font=('bold',14))
endTime.place(x=20, y=120)

pID = Label(root, text="Position ID:", font=('bold',14))
pID.place(x=20, y=150)

#entry and placement for employee ID variable in database
e_eID = Entry()
e_eID.place(x=150, y=30)

#entry and placement for name variable in database
e_name = Entry()
e_name.place(x=150, y=60)

#entry and placement for startTime variable in database
e_startTime = Entry()
e_startTime.place(x=150, y=90)

#entry and placement for endTime variable in database
e_endTime = Entry()
e_endTime.place(x=150, y=120)

e_pID = Entry()
e_pID.place(x=150, y=150)

#insert data into database
insert = Button(root, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=20, y=190)

#delete information from database
delete = Button(root, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=100, y=190)

#update inforamtion from database
update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=180, y=190)

#gets information from database
get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=260, y=190)

#employeeList = Listbox(root, height=9, width=50, border=0)
#employeeList.place(x=550, y=200)

#scrollbar = Scrollbar(root)
#scrollbar.place(x=650, y=200)

#employeeList.configure(yscrollcommand=scrollbar.set)
#scrollbar.configure(command=employeeList.yview)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

trev = ttk.Treeview(columns=(1,2,3,4), show="headings", height="13")
trev.place(x=10, y=220)

trev.heading(1, text="Employee ID")
trev.heading(2, text="Name")
trev.heading(3, text="Start Time")
trev.heading(4, text="End Time")

sql = "SELECT * FROM Employee ORDER BY eID ASC"
cursor.execute(sql)
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

root.mainloop()