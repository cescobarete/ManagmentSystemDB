from tkinter import *
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def populate_list():
    print('Populate')

def add_item():
    ID_text = ID_entry.get()
    part_text = part_entry.get()
    start_text = start_entry.get()
    end_text = end_entry.get()

    if (ID_text=="" or part_text=="" or start_text=="" or end_text==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Employee VALUES('"+eID+"','"+name+"','"+startTime+"','"+endTime+"')")
        cursor.execute("Commit")

        MessageBox.showinfor("Insert Status", "Inserted Successfully")
        con.close()

def remove_item():
    print('remove')

def update_item():
    print('update')

def clear_text():
    print('Clear')

#create window object
app =Tk()


#part employee ID
ID_text = StringVar()
ID_label = Label(app, text='Employee ID:', font=('bold',14))
ID_label.grid(row=0, column=0, sticky=W)
ID_entry = Entry(app, textvariable=ID_text)
ID_entry.grid(row=0, column=1)
#part name
part_text = StringVar()
part_label = Label(app, text='Name:', font=('bold',14),pady=20)
part_label.grid(row=0, column=2, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=3)
#part start time
start_text = StringVar()
start_label = Label(app, text='Start Time:', font=('bold',14))
start_label.grid(row=1, column=0, sticky=W)
start_entry = Entry(app, textvariable=start_text)
start_entry.grid(row=1, column=1)
#part end time
end_text = StringVar()
end_label = Label(app, text='End Time:', font=('bold',14))
end_label.grid(row=1, column=2, sticky=W)
end_entry = Entry(app, textvariable=end_text)
end_entry.grid(row=1, column=3)
#part position
#position_text = StringVar()
#position_label = Label(app, text='Position: ', font=('bold',14),pady=20)
#position_label.grid(row=2, column=0, sticky=W)
#position_entry = Entry(app, textvariable=position_text)
#position_entry.grid(row=2, column=1)
# Name list 
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
#set scroll to list box
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Buttons
add_btn = Button(app, text='Add', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Remove', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(app, text="Clear", width=12, command=clear_text)
clear_btn.grid(row=3, column=3)

#Title and gui size
app.title("Management System")
app.geometry('700x350')

populate_list()

#start program
app.mainloop()