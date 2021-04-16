import tkinter
from tkinter import *
from tkinter import ttk

import tkinter.messagebox as MessageBox
from tkinter.messagebox import askyesno

import mysql.connector as mysql
from mysql.connector import errorcode

#connects database to program, requires localhost, user, password, and db name
con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#insert data into company table
def insertThree():
    pID = p_pID.get()
    position = p_position.get()
    privilege = p_privilege.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get('1.0','end')

    answer = askyesno(title='Confirmation', message='Insert personal information?')
    if answer:

        if (pID=="" or position=="" or positionTaken=="" or directive=="" or privilege==""): #needs these parameters to execute
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Company VALUES('"+pID+"','"+position+"','"+privilege+"','"+positionTaken+"','"+directive+"')")
            cursor.execute("commit")

            p_pID.delete(0, 'end')
            p_position.delete(0, 'end')
            p_privilege.delete(0, 'end')
            p_positionTaken.delete(0, 'end')
            p_directive.delete('1.0', 'end')
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

#deletes company table
def deleteThree():
    answer = askyesno(title='Confirmation', message='Delete this personal information?')
    if answer:

        if(p_pID.get() == ''): #if parameter delete the id and inofmation belonging to it
            MessageBox.showinfo("Delete status","Deleted")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("DELETE FROM Company WHERE pID='"+p_pID.get()+"'")
            cursor.execute("commit")

            p_pID.delete(0, 'end')
            p_position.delete(0, 'end')
            p_privilege.delete(0, 'end')
            p_positionTaken.delete(0, 'end')
            p_directive.delete('1.0', 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

#updates company table
def updateThree():
    pID = p_pID.get()
    position = p_position.get()
    privilege = p_privilege.get()
    positionTaken = p_positionTaken.get()
    directive = p_directive.get('1.0','end')

    answer = askyesno(title='Confirmation', message='Update personal information?')
    if answer:

        if (pID=="" or position=="" or positionTaken=="" or directive=="" or privilege==""): #needs all parameters to update even if all of them are not changed does NOT updates id
            MessageBox.showinfo("Update Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("UPDATE Company SET position='"+position+"', privilege='"+privilege+"', positionTaken='"+positionTaken+"', directive='"+directive+"' WHERE pID='"+pID+"'")
            cursor.execute("commit")

            p_pID.delete(0, 'end')
            p_position.delete(0, 'end')
            p_privilege.delete(0, 'end')
            p_positionTaken.delete(0, 'end')
            p_directive.delete('1.0', 'end')
            MessageBox.showinfo("Update Status", "Update Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")
#gets the data fror company table
def getThree():
    if (p_pID.get() == ""): #needs id to retrieve data, makes it easy to use the other features just by saving time with typing
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Company WHERE pID='"+p_pID.get()+"'")
        rows = cursor.fetchall()

        #inserts each parameter into each text input box from get
        for row in rows: 
            p_position.insert(0, row[1])
            p_privilege.insert(0, row[2])
            p_positionTaken.insert(0, row[3])
            p_directive.insert('1.0', row[4])

        con.close()

#insert into employee table
def insertTwo(): 
    eID = e_eID.get()
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()
    schedule_create = e_schedule_create.get()
    mon = e_mon.get()
    tue = e_tue.get()
    wed = e_wed.get()
    thur = e_thur.get()
    fri = e_fri.get()
    sat = e_sat.get()
    sun = e_sun.get()

    #Message box gives a yes or no option for confirmation
    answer = askyesno(title='Confirmation', message='Insert this employee?')
    if answer:

        if (eID=="" or name==""): #need all parameters to insert
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Employee VALUES('"+eID+"','"+name+"','"+startTime+"','"+endTime+"','"+schedule_create+"','"+mon+"','"+tue+"','"+wed+"','"+thur+"','"+fri+"','"+sat+"','"+sun+"')")
            cursor.execute("commit")

            #Deletes duplicate data if there is any
            e_eID.delete(0, 'end')
            e_name.delete(0, 'end')
            e_startTime.delete(0, 'end')
            e_endTime.delete(0, 'end')
            e_schedule_create.delete(0, 'end')
            e_mon.delete(0, 'end')
            e_tue.delete(0, 'end')
            e_wed.delete(0, 'end')
            e_thur.delete(0, 'end')
            e_fri.delete(0, 'end')
            e_sat.delete(0, 'end')
            e_sun.delete(0, 'end')
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Insert status","Failed")

#delete in employee table 
def deleteTwo():
    answer = askyesno(title='Confirmation', message='Delete this employee?')
    if answer:
        #needs id to specify which info is deleted
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
            e_schedule_create.delete(0, 'end')
            e_mon.delete(0, 'end')
            e_tue.delete(0, 'end')
            e_wed.delete(0, 'end')
            e_thur.delete(0, 'end')
            e_fri.delete(0, 'end')
            e_sat.delete(0, 'end')
            e_sun.delete(0, 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

#update employee table info
def updateTwo(): 
    #grabs information
    eID = e_eID.get()
    name = e_name.get()
    startTime = e_startTime.get()
    endTime = e_endTime.get()
    schedule_create = e_schedule_create.get()
    mon = e_mon.get()
    tue = e_tue.get()
    wed = e_wed.get()
    thur = e_thur.get()
    fri = e_fri.get()
    sat = e_sat.get()
    sun = e_sun.get()

    answer = askyesno(title='Confirmation', message='Update this employee?')
    if answer:

        if (eID=="" or name=="" or startTime=="" or endTime=="" or schedule_create=="" or mon=="" or tue=="" or wed=="" or thur=="" or fri=="" or sat=="" or sun==""): #needs all fields to be filled or dont execute
            MessageBox.showinfo("Update Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("UPDATE Employee SET name='"+name+"', startTime='"+startTime+"', endTime='"+endTime+"', schedule_create='"+schedule_create+"', mon='"+mon+"', tue='"+tue+"', wed='"+wed+"', thur='"+thur+"', fri='"+fri+"', sat='"+sat+"', sun='"+sun+"' WHERE eID='"+eID+"'")
            cursor.execute("commit")

            e_eID.delete(0, 'end') #if duplicate dont update
            e_name.delete(0, 'end')
            e_startTime.delete(0, 'end')
            e_endTime.delete(0, 'end')
            e_schedule_create.delete(0, 'end')
            e_mon.delete(0, 'end')
            e_tue.delete(0, 'end')
            e_wed.delete(0, 'end')
            e_thur.delete(0, 'end')
            e_fri.delete(0, 'end')
            e_sat.delete(0, 'end')
            e_sun.delete(0, 'end')

            MessageBox.showinfo("Update Status", "Update Successfully")
            con.close()
    else:
        MessageBox.showinfo("Update status","Failed")     
#gets employee table info
def getTwo(): 
    #needs employee id to get info
    if (e_eID.get() == ""): 
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
            e_schedule_create.insert(0, row[4])
            e_mon.insert(0, row[5])
            e_tue.insert(0, row[6])
            e_wed.insert(0, row[7])
            e_thur.insert(0, row[8])
            e_fri.insert(0, row[9])
            e_sat.insert(0, row[10])
            e_sun.insert(0, row[11])

        con.close()

#inserts into personal info table
def insert():
    eIDTwo = d_eID.get()
    pIDTwo = d_pID.get()
    yearlySalary = d_yearlySalary.get()
    email = d_email.get()
    phone = d_phone.get()
    ssn = d_ssn.get()
    city = d_city.get()
    adr = d_adr.get()
    zip = d_zip.get()
    review = d_review.get('1.0','end')

    answer = askyesno(title='Confirmation', message='Insert this position?')
    if answer:
        
        #needs all of these parameters to insert data, the get function 
        if (eIDTwo=="" or pIDTwo=="" or yearlySalary=="" or email=="" or phone=="" or ssn=="" or city=="" or adr=="" or zip==""): 
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            cursor.execute("INSERT INTO PersonalInfo VALUES('"+eIDTwo+"','"+pIDTwo+"','"+yearlySalary+"','"+email+"','"+phone+"','"+ssn+"','"+city+"','"+adr+"','"+zip+"','"+review+"')")
            cursor.execute("commit")

            d_eID.delete(0, 'end')
            d_pID.delete(0, 'end')
            d_yearlySalary.delete(0, 'end')
            d_email.delete(0, 'end')
            d_phone.delete(0, 'end')
            d_ssn.delete(0, 'end')
            d_city.delete(0, 'end')
            d_adr.delete(0, 'end')
            d_zip.delete(0, 'end')
            d_review.delete('1.0', 'end')
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Insert status","Failed")

#update personal info table
def update(): 
    eID = d_eID.get()
    pID = d_pID.get()
    yearlySalary = d_yearlySalary.get()
    email = d_email.get()
    phone = d_phone.get()
    ssn = d_ssn.get()
    city = d_city.get()
    adr = d_adr.get()
    zip = d_zip.get()
    review = d_review.get('1.0','end')

    answer = askyesno(title='Confirmation', message='Update this position?')
    if answer:

        if (eID=="" or pID=="" or yearlySalary=="" or email=="" or phone=="" or ssn=="" or city=="" or adr=="" or zip==""):
            MessageBox.showinfo("Update Status", "All Fields are required")
        else:
            con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
            cursor = con.cursor()
            #allows to update pid if employee changes positions but not the employee id
            cursor.execute("UPDATE PersonalInfo SET pID='"+pID+"',yearlySalary='"+yearlySalary+"', email='"+email+"', phone='"+phone+"', ssn='"+ssn+"', city='"+city+"', adr='"+adr+"', zip='"+zip+"', review='"+review+"' WHERE eID='"+eID+"' AND pID='"+pID+"'") 
            cursor.execute("commit")

            d_eID.delete(0, 'end')
            d_pID.delete(0, 'end')
            d_yearlySalary.delete(0, 'end')
            d_email.delete(0, 'end')
            d_phone.delete(0, 'end')
            d_ssn.delete(0, 'end')
            d_city.delete(0, 'end')
            d_adr.delete(0, 'end')
            d_zip.delete(0, 'end')
            d_review.delete('1.0','end')
            MessageBox.showinfo("Update Status", "Update Successfully")
            con.close()
    else:
        MessageBox.showinfo("Update status","Failed")

#delete in employee table
def delete():

    answer = askyesno(title='Confirmation', message='Delete this position?')
    if answer:

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
            d_phone.delete(0, 'end')
            d_ssn.delete(0, 'end')
            d_city.delete(0, 'end')
            d_adr.delete(0, 'end')
            d_zip.delete(0, 'end')
            d_review.delete('1.0', 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

#retrieves personal info data
def get(): 
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
            d_phone.insert(0, row[4])
            d_ssn.insert(0, row[5])
            d_city.insert(0, row[6])
            d_adr.insert(0, row[7])
            d_zip.insert(0, row[8])
            d_review.insert('1.0', row[9])
        con.close()

#root window
root = Tk()
#Size of root window
root.geometry("2000x1100")
root.title("Managment System")

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#First panel
p1 = PanedWindow(orient=VERTICAL,bd=4,relief="raised",bg="black", handlesize=100)
p1.pack(fill=BOTH,expand=1)

#database within underleft 
underLeft = Label(p1, height=25)
p1.add(underLeft)

#second panel
p2 = PanedWindow(p1,orient=HORIZONTAL,bd=4,relief="raised",bg="black")
p1.add(p2)

#employee table inside top
top = Label(p2,width=50)
p2.add(top)

#personal information in bottom 
bottom = Label(p2, width=55)
p2.add(bottom)

#company table in left_label box
left_label = Label(p2, width=50)
p2.add(left_label)

#start of employee lable and entries=============================================
#label for fields within employee table
eID = Label(top, text="Employee ID:", font=('bold',14))
eID.place(x=20, y=30)

name = Label(top, text="Name:", font=('bold',14))
name.place(x=20, y=60)

startTime = Label(top, text="Start time:", font=('bold',14))
startTime.place(x=20, y=90)

endTime = Label(top, text="End time:", font=('bold',14))
endTime.place(x=20, y=120)

schedule_create = Label(top, text="Schedule Creation:", font=('bold',14))
schedule_create.place(x=20, y=150)

mon = Label(top, text="Monday:", font=('bold',14))
mon.place(x=20, y=180)

tue = Label(top, text="Tuesday:", font=('bold',14))
tue.place(x=20, y=210)

wed = Label(top, text="Wednesday:", font=('bold',14))
wed.place(x=20, y=240)

thur = Label(top, text="Thursday:", font=('bold',14))
thur.place(x=20, y=270)

fri = Label(top, text="Friday:", font=('bold',14))
fri.place(x=20, y=300)

sat = Label(top, text="Saturday:", font=('bold',14))
sat.place(x=20, y=330)

sun = Label(top, text="Sunday:", font=('bold',14))
sun.place(x=20, y=360)

#entry boxes for empoloyee table
e_eID = Entry(top)
#allows placement for each text entry
e_eID.place(x=150, y=30)

e_name = Entry(top)
e_name.place(x=150, y=60)

e_startTime = Entry(top)
e_startTime.place(x=150, y=90)

e_endTime = Entry(top)
e_endTime.place(x=150, y=120)

e_schedule_create = Entry(top)
e_schedule_create.place(x=150, y=150)

e_mon = Entry(top)
e_mon.place(x=150, y=180)

e_tue = Entry(top)
e_tue.place(x=150, y=210)

e_wed = Entry(top)
e_wed.place(x=150, y=240)

e_thur = Entry(top)
e_thur.place(x=150, y=270)

e_fri = Entry(top)
e_fri.place(x=150, y=300)

e_sat = Entry(top)
e_sat.place(x=150, y=330)

e_sun = Entry(top)
e_sun.place(x=150, y=360)
#end for employee tables===========================================================

#Start of company table entries and labels=========================================
pID = Label(left_label, text="Enter position ID:", font=('bold',14))
pID.place(x=20, y=30)

position = Label(left_label, text="Enter position:", font=('bold',14))
position.place(x=20, y=60)

privilege = Label(left_label, text="Enter privilege:", font=('bold',14))
privilege.place(x=20, y=120)

positionTaken = Label(left_label, text="Taken(yes/no):", font=('bold',14))
positionTaken.place(x=20, y=90)

directive = Label(left_label, text="Directive:", font=('bold',14))
directive.place(x=20, y=150)

p_pID = Entry(left_label)
p_pID.place(x=150, y=30)

p_position = Entry(left_label)
p_position.place(x=150, y=60)

p_privilege = Entry(left_label)
p_privilege.place(x=150, y=120)

p_positionTaken = Entry(left_label)
p_positionTaken.place(x=150, y=90)

p_directive = Text(left_label, width=25, height=10)
p_directive.place(x=152, y=150)
#end of company table============================================================

#Start of personal info entries and labels=======================================
eIDTwo = Label(bottom, text="Enter employee ID:", font=('bold',14))
eIDTwo.place(x=20, y=30)

pIDTwo = Label(bottom, text="Enter position ID:", font=('bold',14))
pIDTwo.place(x=20, y=60)

yearlySalary = Label(bottom, text="Salary:", font=('bold',14))
yearlySalary.place(x=20, y=90)

email = Label(bottom, text="Email:", font=('bold',14))
email.place(x=20, y=120)

phone = Label(bottom, text="Phone #:", font=('bold',14))
phone.place(x=20, y=150)

ssn = Label(bottom, text="SS#:", font=('bold',14))
ssn.place(x=20, y=180)

city = Label(bottom, text="City:", font=('bold',14))
city.place(x=20, y=210)

adr = Label(bottom, text="Address:", font=('bold',14))
adr.place(x=20, y=240)

zip = Label(bottom, text="Zip:", font=('bold',14))
zip.place(x=20, y=270)

review = Label(bottom, text="Review:", font=('bold',14))
review.place(x=20, y=300)

d_eID = Entry(bottom)
d_eID.place(x=150, y=30)

d_pID = Entry(bottom)
d_pID.place(x=150, y=60)

d_yearlySalary = Entry(bottom)
d_yearlySalary.place(x=150, y=90)

d_email = Entry(bottom)
d_email.place(x=150, y=120)

d_phone = Entry(bottom)
d_phone.place(x=150, y=150)

d_ssn = Entry(bottom)
d_ssn.place(x=150, y=180)

d_city = Entry(bottom)
d_city.place(x=150, y=210)

d_adr = Entry(bottom)
d_adr.place(x=150, y=240)

d_zip = Entry(bottom)
d_zip.place(x=150, y=270)

d_review = Text(bottom, width=25, height=10)
d_review.place(x=152, y=300)
#end of personal info entries and labels=========================================

#displays company database
def company_tree():
    left_label = Tk()
    left_label.geometry("200x1100")
    left_label.title("Company Database")
    #company table displaying information within gui
    trevComp = ttk.Treeview(left_label,columns=(1,2,3,4,5), show="headings", height="20")
    trevComp.pack()

    #headings for each piece of info displayed
    trevComp.heading(1, text="Position ID")
    trevComp.heading(2, text="Position")
    trevComp.heading(3, text="Privilege")
    trevComp.heading(4, text="Position Taken")
    trevComp.heading(5, text="Directive")

    #select for info being grabbed from database
    cursor.execute("SELECT * FROM Company")
    rows = cursor.fetchall()

    for i in rows:
        trevComp.insert('','end',values=i)

#start of company table button from here=========================================
insertThree = Button(left_label, text="Insert", font=('italic',10), bg="white", command=insertThree)
insertThree.place(x=350, y=30)

deleteThree = Button(left_label, text="Delete", font=('italic',10), bg="white", command=deleteThree)
deleteThree.place(x=350, y=60)

updateThree = Button(left_label, text="Update", font=('italic',10), bg="white", command=updateThree)
updateThree.place(x=350, y=90)

getThree = Button(left_label, text="Get", font=('italic',10), bg="white", command=getThree)
getThree.place(x=350, y=120)

getCompany = Button(left_label, text="Company Data", font=('italic',10), bg="white", command=company_tree)
getCompany.place(x=350, y=150)
#end company table button to here=================================================

#employee table displaying employee information within gui
def employee_db():
    top = Tk()
    top.title("Employee Database")
    trevEmp = ttk.Treeview(top,columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="20")
    trevEmp.pack()

    #headings for each piece of info displayed
    trevEmp.heading(2, text="Employee ID")
    trevEmp.heading(1, text="Name")
    trevEmp.heading(3, text="Start Time")
    trevEmp.heading(4, text="End Time")
    trevEmp.heading(5, text="Schedule Created")
    trevEmp.heading(6, text="Monday")
    trevEmp.heading(7, text="Tuesday")
    trevEmp.heading(8, text="Wednesday")
    trevEmp.heading(9, text="Thursday")
    trevEmp.heading(10, text="Friday")
    trevEmp.heading(11, text="Saturday")
    trevEmp.heading(12, text="Sunday")

    #select for info being grabbed from database
    cursor.execute("SELECT * FROM Employee")
    rows = cursor.fetchall()

    for i in rows:
        trevEmp.insert('','end',values=i)

#start of employee table buttons from here========================================
#insert data into database
insertTwo = Button(top, text="Insert", font=('italic',10), bg="white", command=insertTwo)
insertTwo.place(x=350, y=30)

#delete information from database
deleteTwo = Button(top, text="Delete", font=('italic',10), bg="white", command=deleteTwo)
deleteTwo.place(x=350, y=60)

#update inforamtion from database
updateTwo = Button(top, text="Update", font=('italic',10), bg="white", command=updateTwo)
updateTwo.place(x=350, y=90)

#gets information from database
getTwo = Button(top, text="Get", font=('italic',10), bg="white", command=getTwo)
getTwo.place(x=350, y=120)

getEmployee = Button(top, text="Employee Data", font=('italic',10), bg="white", command=employee_db)
getEmployee.place(x=350, y=150)
#employee table button to here====================================================

#displays personal infromation database
def pi_tree():
    bottom = Tk()
    bottom.title("Perosnal Information Database")
    #personal info table displaying information within gui
    trevPI = ttk.Treeview(bottom,columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="20")
    trevPI.pack()

    #headings for each piece of info displayed
    trevPI.heading(1, text="Employee ID")
    trevPI.heading(2, text="Position ID")
    trevPI.heading(3, text="Salary")
    trevPI.heading(4, text="E-mail")
    trevPI.heading(5, text="Phone")
    trevPI.heading(6, text="SSN")
    trevPI.heading(7, text="City")
    trevPI.heading(8, text="Address")
    trevPI.heading(9, text="Zip")
    trevPI.heading(10, text="Review")

    #select for info being grabbed from database
    cursor.execute("SELECT * FROM PersonalInfo")
    rows = cursor.fetchall()

    for i in rows:
        trevPI.insert('','end',values=i)

#start of personal info table button from here=======================================
insert = Button(bottom, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=350, y=30)

update = Button(bottom, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=350, y=60)

delete = Button(bottom, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=350, y=90)

get = Button(bottom, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=350, y=120)

getPI = Button(bottom, text="Personal Info Data", font=('italic',10), bg="white", command=pi_tree)
getPI.place(x=350, y=150)
#end of personal info table button from here=======================================

#Shows relevant information to management of employees within system
trev = ttk.Treeview(underLeft,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), show="headings", height="15")

#headings for each piece of info displayed
trev.heading(1, text="Name")
trev.heading(2, text="Employee ID")
trev.heading(5, text="Start Time")
trev.heading(6, text="End Time")
trev.heading(7, text="Scedule Created")
trev.heading(8, text="Monday")
trev.heading(9, text="Tuesday")
trev.heading(10, text="Wednesday")
trev.heading(11, text="Thursday")
trev.heading(12, text="Friday")
trev.heading(13, text="Saturday")
trev.heading(14, text="Sunday")
trev.heading(3, text="Position ID")
trev.heading(4, text="Position")
trev.heading(15, text="Salary")
trev.heading(16, text="E-mail")

#select for info being grabbed from database
cursor.execute("SELECT name, Employee.eID, Company.pID, position, startTime, endTime, schedule_create, mon, tue, wed, thur, fri, sat, sun, yearlySalary, email FROM Employee, Company, PersonalInfo WHERE Employee.eID = PersonalInfo.eID AND Company.pID = PersonalInfo.pID ORDER BY eID ASC")
rows = cursor.fetchall()

for i in rows:
    trev.insert('','end',values=i)

#horizontal scrollbar for database 
hsb = ttk.Scrollbar(underLeft,orient="horizontal")
hsb.configure(command=trev.xview)
trev.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

#vertical scrollbar for database
hsb = ttk.Scrollbar(underLeft,orient="vertical")
hsb.configure(command=trev.yview)
trev.configure(yscrollcommand=hsb.set)
hsb.pack(fill=Y,side=RIGHT)

trev.pack()

root.mainloop()