import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

fd = open('managmentDatabase.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')

for command in sqlCommands:
    try:
        if command.strip() != '':
            cursor.execute(command)
    except IOError:
        print ("Command skipped: ", msg)

executeScriptsFromFile('/Users/cescobarete/Documents/Spring2021/CAPSTONE/ManagmentSystemDB')
con.commit()

def insertThree(): #insert data into company table
    pID = p_pID.get()
    position = p_position.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get()

    if (pID=="" or position=="" or positionTaken=="" or directive==""): #needs these parameters to execute
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
    
def deleteThree(): #deletes company table
    if(p_pID.get() == ''): #if parameter delete the id and inofmation belonging to it
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


def updateThree(): #updates company table
    pID = p_pID.get()
    position = p_position.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get()

    if (pID=="" or position=="" or positionTaken=="" or directive==""): #needs all parameters to update even if all of them are not changed does NOT updates id
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

def getThree(): #gets the data fror company table
    if (p_pID.get() == ""): #needs id to retrieve data, makes it easy to use the other features just by saving time with typing
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Company WHERE pID='"+p_pID.get()+"'")
        rows = cursor.fetchall()

        for row in rows: #inserts each parameter into each text input box
            p_position.insert(0, row[1])
            p_positionTaken.insert(0, row[2])
            p_directive.insert(0, row[3])

        con.close()


def insertTwo(): #insert into employee table
    eID = e_eID.get()
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()

    if (eID=="" or name=="" or startTime=="" or endTime==""): #need all parameters to insert
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
    
def deleteTwo(): #delete in employee table
    if(e_eID.get() == ''): #needs id to specify which info is deleted
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

def updateTwo(): #update employee table info
    eID = e_eID.get() #grabs information
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()

    if (eID=="" or name=="" or startTime=="" or endTime==""): #needs all fields to be filled or dont execute
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("UPDATE Employee SET name='"+name+"', startTime='"+startTime+"', endTime='"+endTime+"' WHERE eID='"+eID+"'")
        cursor.execute("commit")

        e_eID.delete(0, 'end') #if duplicate dont update
        e_name.delete(0, 'end')
        e_startTime.delete(0, 'end')
        e_endTime.delete(0, 'end')

        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def getTwo(): #gets employee table info
    if (e_eID.get() == ""): #needs employee id to get info
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Employee WHERE eID='"+e_eID.get()+"'")
        rows = cursor.fetchall()

        for row in rows: #rows are inserted into each text box after the 0 text box that would be eID
            e_name.insert(0, row[1])
            e_startTime.insert(0, row[2])
            e_endTime.insert(0, row[3])

        con.close()

def insert(): #inserts into personal info table
    eIDTwo = d_eID.get()
    pIDTwo = d_pID.get()
    yearlySalary = d_yearlySalary.get()
    email = d_email.get()
    review = d_review.get()

    if (eIDTwo=="" or pIDTwo=="" or yearlySalary=="" or email==""): #needs all of these parameters to insert data, the get function 
                                                                    #makes it easy to retrieve and change if not a lot to change
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

def update(): #update personal info table
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
        #allows to update pid if employee changes positions but not the employee id
        cursor.execute("UPDATE PersonalInfo SET pID='"+pID+"',yearlySalary='"+yearlySalary+"', email='"+email+"', review='"+review+"' WHERE eID='"+eID+"' AND pID='"+pID+"'") 
        cursor.execute("commit")

        d_eID.delete(0, 'end')
        d_pID.delete(0, 'end')
        d_yearlySalary.delete(0, 'end')
        d_email.delete(0, 'end')
        d_review.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def delete(): #delete in employee table
    if(d_eID.get()=='' and d_pID.get()==''): #needs both id to specify which info is deleted
        MessageBox.showinfo("Delete status","Deleted")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("DELETE FROM PersonalInfo WHERE eID='"+d_eID.get()+"' and pID='"+d_pID.get()+"'")
        cursor.execute("commit")

        d_eID.delete(0, 'end')
        d_pID.delete(0, 'end')
        d_yearlySalary.delete(0, 'end')
        d_email.delete(0, 'end')
        d_review.delete(0, 'end')
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def get(): #retrieves personal info data
    if (d_eID.get() == "" and d_pID.get() == ""): #needs both employee id and company position id
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

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#First panel
p1 = PanedWindow(orient=VERTICAL,bd=4,relief="raised",bg="black", handlesize=100)
p1.pack(fill=BOTH,expand=1)

underLeft = Label(p1, height=25)
p1.add(underLeft)

#second panel
p2 = PanedWindow(p1,orient=HORIZONTAL,bd=4,relief="raised",bg="black")
p1.add(p2)

top = Label(p2,width=50)
p2.add(top)

bottom = Label(p2, width=55)
p2.add(bottom)

left_label = Label(p2, width=50)
p2.add(left_label)
#start of employee lable and entries===============================
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
#end of entry and labels for employee tables==================

#Start of company table entried and labels====================
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
#end of company table entryies and labels==========================

#Start of personal info entries and labels=========================
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
#end of personal info entries and labels=========================

#start of company table button from here==================================
insertThree = Button(left_label, text="Insert", font=('italic',10), bg="white", command=insertThree)
insertThree.place(x=20, y=190)

deleteThree = Button(left_label, text="Delete", font=('italic',10), bg="white", command=deleteThree)
deleteThree.place(x=80, y=190)

updateThree = Button(left_label, text="Update", font=('italic',10), bg="white", command=updateThree)
updateThree.place(x=140, y=190)

getThree = Button(left_label, text="Get", font=('italic',10), bg="white", command=getThree)
getThree.place(x=200, y=190)
#end company table button to here========================================

#company table displaying information within gui
trevComp = ttk.Treeview(left_label,columns=(1,2,3,4), show="headings", height="20")
trevComp.place(x=350, y=10)

#headings for each piece of info displayed
trevComp.heading(1, text="Position ID")
trevComp.heading(2, text="Position")
trevComp.heading(3, text="Position Taken")
trevComp.heading(4, text="Directive")

#select for info being grabbed from database
cursor.execute("SELECT * FROM Company")
rows = cursor.fetchall()

for i in rows:
    trevComp.insert('','end',values=i)

#start of employee table buttons from here=========================
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
#employee table button to here====================================

#employee table displaying employee information within gui
trevEmp = ttk.Treeview(top,columns=(1,2,3,4), show="headings", height="20")
trevEmp.place(x=350, y=10)

#headings for each piece of info displayed
trevEmp.heading(2, text="Employee ID")
trevEmp.heading(1, text="Name")
trevEmp.heading(3, text="Start Time")
trevEmp.heading(4, text="End Time")

#select for info being grabbed from database
cursor.execute("SELECT * FROM Employee")
rows = cursor.fetchall()

for i in rows:
    trevEmp.insert('','end',values=i)

#start of personal info table button from here=======================================
insert = Button(bottom, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=20, y=190)

update = Button(bottom, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=80, y=190)

delete = Button(bottom, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=140, y=190)

get = Button(bottom, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=200, y=190)
#end of personal info table button from here=======================================

#personal info table displaying information within gui
trevPI = ttk.Treeview(bottom,columns=(1,2,3,4,5), show="headings", height="20")
trevPI.place(x=350, y=10)

#headings for each piece of info displayed
trevPI.heading(1, text="Employee ID")
trevPI.heading(2, text="Position ID")
trevPI.heading(3, text="Salary")
trevPI.heading(4, text="E-mail")
trevPI.heading(5, text="Review")

#select for info being grabbed from database
cursor.execute("SELECT * FROM PersonalInfo")
rows = cursor.fetchall()

for i in rows:
    trevPI.insert('','end',values=i)

#database displaying information within gui
trev = ttk.Treeview(underLeft,columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="20")

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
trev.heading(10, text="Review")

#select for info being grabbed from database
cursor.execute("SELECT name, Employee.eID, startTime, endTime, Company.pID, position, yearlySalary, email, directive, review FROM Employee, Company, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID ORDER BY eID ASC")
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

hsb = ttk.Scrollbar(underLeft,orient="horizontal")
hsb.configure(command=trev.xview)
trev.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

hsb = ttk.Scrollbar(underLeft,orient="vertical")
hsb.configure(command=trev.yview)
trev.configure(yscrollcommand=hsb.set)
hsb.pack(fill=Y,side=RIGHT)

trev.pack()

root.mainloop()