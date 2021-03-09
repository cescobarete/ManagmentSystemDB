import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def insertThree():
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
    
def deleteThree():
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


def updateThree():
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

def getThree():
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


def insertTwo():
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
    
def deleteTwo():
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

def updateTwo():
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

def getTwo():
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

def insert():
    eIDTwo = d_eID.get()
    pIDTwo = d_pID.get()
    yearlySalary = d_yearlySalary.get()
    email = d_email.get()
    review = d_review.get()

    if (eIDTwo=="" or pIDTwo=="" or yearlySalary=="" or email==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("INSERT INTO PersonalInfo VALUES('"+eIDTwo+"','"+pIDTwo+"','"+yearlySalary+"','"+email+"','"+review+"')")
        cursor.execute("commit")

        d_eID.delete(0, 'end')
        d_pID.delete(0, 'end')
        d_yearlySalary.delete(0, 'end')
        d_email.delete(0, 'end')
        d_review.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

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
        cursor.execute("UPDATE PersonalInfo SET pID='"+pID+"',yearlySalary='"+yearlySalary+"', email='"+email+"', review='"+review+"' WHERE eID='"+eID+"' AND pID='"+pID+"'")
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
root.geometry("2000x1100")
root.title("Managment System")

#First panel
p1 = PanedWindow(orient=VERTICAL,bd=4,relief="raised",bg="black", handlesize=100)
p1.pack(fill=BOTH,expand=1)

underLeft = Label(p1, height=30)
p1.add(underLeft)

#second panel
p2 = PanedWindow(p1,orient=HORIZONTAL,bd=4,relief="raised",bg="black")
p1.add(p2)

top = Label(p2,width=55)
p2.add(top)

bottom = Label(p2, width=55)
p2.add(bottom)

left_label = Label(p2, width=55)
p2.add(left_label)

#label inserts what the entry does in the program
eID = Label(top, text="Employee ID:", font=('bold',14))
eID.place(x=20, y=30)

name = Label(top, text="Name:", font=('bold',14))
name.place(x=20, y=60)

startTime = Label(top, text="Start time:", font=('bold',14))
startTime.place(x=20, y=90)

endTime = Label(top, text="End time:", font=('bold',14))
endTime.place(x=20, y=120)

#entry and placement for employee ID variable in database
e_eID = Entry(top)
e_eID.place(x=150, y=30)

#entry and placement for name variable in database
e_name = Entry(top)
e_name.place(x=150, y=60)

#entry and placement for startTime variable in database
e_startTime = Entry(top)
e_startTime.place(x=150, y=90)

#entry and placement for endTime variable in database
e_endTime = Entry(top)
e_endTime.place(x=150, y=120)

#Start of company
pID = Label(left_label, text="Enter position ID:", font=('bold',14))
pID.place(x=20, y=30)

position = Label(left_label, text="Enter position:", font=('bold',14))
position.place(x=20, y=60)

positionTaken = Label(left_label, text="Taken(yes/no):", font=('bold',14))
positionTaken.place(x=20, y=90)

directive = Label(left_label, text="Directive:", font=('bold',14))
directive.place(x=20, y=120)

p_pID = Entry(left_label)
p_pID.place(x=150, y=30)

p_position = Entry(left_label)
p_position.place(x=150, y=60)

p_positionTaken = Entry(left_label)
p_positionTaken.place(x=150, y=90)

p_directive = Entry(left_label)
p_directive.place(x=150, y=120)

#Start of personal info
eIDTwo = Label(bottom, text="Enter employee ID:", font=('bold',14))
eIDTwo.place(x=20, y=30)

pIDTwo = Label(bottom, text="Enter position ID:", font=('bold',14))
pIDTwo.place(x=20, y=60)

yearlySalary = Label(bottom, text="Salary:", font=('bold',14))
yearlySalary.place(x=20, y=90)

email = Label(bottom, text="Email:", font=('bold',14))
email.place(x=20, y=120)

review = Label(bottom, text="Review:", font=('bold',14))
review.place(x=20, y=150)

d_eID = Entry(bottom)
d_eID.place(x=150, y=30)

d_pID = Entry(bottom)
d_pID.place(x=150, y=60)

d_yearlySalary = Entry(bottom)
d_yearlySalary.place(x=150, y=90)

d_email = Entry(bottom)
d_email.place(x=150, y=120)

d_review = Entry(bottom)
d_review.place(x=150, y=150)

insertThree = Button(left_label, text="Insert", font=('italic',10), bg="white", command=insertThree)
insertThree.place(x=20, y=190)

deleteThree = Button(left_label, text="Delete", font=('italic',10), bg="white", command=deleteThree)
deleteThree.place(x=80, y=190)

updateThree = Button(left_label, text="Update", font=('italic',10), bg="white", command=updateThree)
updateThree.place(x=140, y=190)

getThree = Button(left_label, text="Get", font=('italic',10), bg="white", command=getThree)
getThree.place(x=200, y=190)

#insert data into database
insertTwo = Button(top, text="Insert", font=('italic',10), bg="white", command=insertTwo)
insertTwo.place(x=20, y=190)

#delete information from database
deleteTwo = Button(top, text="Delete", font=('italic',10), bg="white", command=deleteTwo)
deleteTwo.place(x=80, y=190)

#update inforamtion from database
updateTwo = Button(top, text="Update", font=('italic',10), bg="white", command=updateTwo)
updateTwo.place(x=140, y=190)

#gets information from database
getTwo = Button(top, text="Get", font=('italic',10), bg="white", command=getTwo)
getTwo.place(x=200, y=190)

insert = Button(bottom, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=20, y=190)

update = Button(bottom, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=80, y=190)

get = Button(bottom, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=140, y=190)

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

trev = ttk.Treeview(underLeft,columns=(1,2,3,4,5,6,7,8), show="headings", height="20")
trev.place(x=10, y=10)

trev.heading(2, text="Employee ID")
trev.heading(1, text="Name")
trev.heading(3, text="Start Time")
trev.heading(4, text="End Time")
trev.heading(5, text="Position ID")
trev.heading(6, text="Position")
trev.heading(7, text="Salary")
trev.heading(8, text="E-mail")

sql = "SELECT name, Employee.eID, startTime, endTime, Company.pID, position, yearlySalary, email, directive, review FROM Employee, Company, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID ORDER BY eID ASC"
cursor.execute(sql)
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

root.mainloop()