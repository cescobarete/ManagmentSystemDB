import os

import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def UploadCompany():
    os.system("python3 gui_company.py")

def UploadPersonalInfo():
    os.system("python3 gui_personalinfo.py")

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

    #needs all fields to be filled or dont execute
    if (eID=="" or name=="" or startTime=="" or endTime==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("UPDATE Employee SET name='"+name+"', startTime='"+startTime+"', endTime='"+endTime+"' WHERE eID='"+eID+"'")
        cursor.execute("commit")

        #if duplicate dont update
        e_eID.delete(0, 'end')
        e_name.delete(0, 'end')
        e_startTime.delete(0, 'end')
        e_endTime.delete(0, 'end')
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
eID = Label(root, text="Enter employee ID:", font=('bold',14))
eID.place(x=20, y=30)

name = Label(root, text="Enter name:", font=('bold',14))
name.place(x=20, y=60)

startTime = Label(root, text="Enter start time:", font=('bold',14))
startTime.place(x=20, y=90)

endTime = Label(root, text="Enter end time:", font=('bold',14))
endTime.place(x=20, y=120)

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

#insert data into database
insert = Button(root, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=20, y=160)

#delete information from database
delete = Button(root, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=100, y=160)

#update inforamtion from database
update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=180, y=160)

#gets information from database
get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=260, y=160)

#executes company gui table
openCompany = Button(root, text='Open Comapny Table', font=('italic',10), bg="white", command=UploadCompany)
openCompany.place(x=340, y=160)

#executes personal inforamtion gui table
openPersonalInfo= Button(root, text='Open Perosnal Info Table', font=('italic',10), bg="white", command=UploadPersonalInfo)
openPersonalInfo.place(x=500, y=160)

root.mainloop()