import os

import time
import threading

import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def GetDisplay():
    os.system("python3 gui_display.py")

def UploadEmployee():
    os.system("python3 gui_employee.py")

def UploadCompany():
    #time.sleep(2)
    os.system("python3 gui_company.py")

def UploadPersonalInfo():
    os.system("python3 gui_personalinfo.py")

root = Tk()
root.geometry("700x500")
root.title("Managment System: Main")

#executes employee gui table
openEmployee = Button(root, text='Open Employee Table', font=('italic',10), bg="white", command=UploadEmployee)
openEmployee.place(x=180, y=460)

#executes company gui table
openCompany = Button(root, text='Open Comapny Table', font=('italic',10), bg="white", command=UploadCompany)
openCompany.place(x=340, y=460)

#executes personal inforamtion gui table
openPersonalInfo = Button(root, text='Open Perosnal Info Table', font=('italic',10), bg="white", command=UploadPersonalInfo)
openPersonalInfo.place(x=500, y=460)

#openData = Button(root, text='Open Database', font=('italic',10), bg="white", command=threading.Thread(target=GetDisplay).start())
openData = Button(root, text='Open Database', font=('italic',10), bg="white", command=GetDisplay)
openData.place(x=20, y=460)

root.mainloop()