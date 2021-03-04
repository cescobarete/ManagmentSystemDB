import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def insert():
    pID = p_pID.get()
    position = p_position.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get()

    if (pID=="" or position=="" or positionTaken=="" or directive==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Company VALUES('"+pID+"','"+position+"','"+positionTaken+"','"+directive+"')")
        cursor.execute("commit")

        p_pID.delete(0, 'end')
        p_position.delete(0, 'end')
        p_positionTaken.delete(0, 'end')
        p_directive.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()
    
def delete():
    if(p_pID.get() == ''):
        MessageBox.showinfo("Delete status","Deleted")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("DELETE FROM Company WHERE pID='"+p_pID.get()+"'")
        cursor.execute("commit")

        p_pID.delete(0, 'end')
        p_position.delete(0, 'end')
        p_positionTaken.delete(0, 'end')
        p_directive.delete(0, 'end')
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()


def update():
    pID = p_pID.get()
    position = p_position.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get()

    if (pID=="" or position=="" or positionTaken=="" or directive==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("UPDATE Company SET position='"+position+"', positionTaken='"+positionTaken+"', directive='"+directive+"' WHERE pID='"+pID+"'")
        cursor.execute("commit")

        p_pID.delete(0, 'end')
        p_position.delete(0, 'end')
        p_positionTaken.delete(0, 'end')
        p_directive.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def get():
    if (p_pID.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Company WHERE pID='"+p_pID.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            p_position.insert(0, row[1])
            p_positionTaken.insert(0, row[2])
            p_directive.insert(0, row[3])

        con.close()

root = Tk()
root.geometry("700x500")
root.title("Managment System: Company")

pID = Label(root, text="Enter position ID:", font=('bold',14))
pID.place(x=20, y=30)

position = Label(root, text="Enter position:", font=('bold',14))
position.place(x=20, y=60)

positionTaken = Label(root, text="Taken(yes/no)", font=('bold',14))
positionTaken.place(x=20, y=90)

directive = Label(root, text="Directive:", font=('bold',14))
directive.place(x=20, y=120)

p_pID = Entry()
p_pID.place(x=150, y=30)

p_position = Entry()
p_position.place(x=150, y=60)

p_positionTaken = Entry()
p_positionTaken.place(x=150, y=90)

p_directive = Entry()
p_directive.place(x=150, y=120)

insert = Button(root, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=20, y=170)

delete = Button(root, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=100, y=170)

update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=180, y=170)

get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=260, y=170)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

trev = ttk.Treeview(columns=(1,2,3,4,5), show="headings", height="13")
trev.place(x=10, y=220)

trev.heading(1, text="Name")
trev.heading(2, text="Position ID")
trev.heading(3, text="Position")
trev.heading(4, text="Position Taken")
trev.heading(5, text="Directive")

sql = "SELECT name, Company.pID, position, positionTaken, directive FROM Company, Employee, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID"
cursor.execute(sql)
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

root.mainloop()