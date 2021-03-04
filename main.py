import os

import time
import threading

import tkinter
from tkinter import *
import tkinter.messagebox as MessageBox

import mysql.connector as mysql
from mysql.connector import errorcode

def database():
    con = mysql.connector.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
    mycursor = con.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS ManageEmp")
    mycursor.execute("commit")
    mycursor.execute("drop table if exists PersonalInfo")
    mycursor.execute("drop table if exists Company")
    mycursor.execute("drop table if exists Employee")
    mycursor.execute("create table Employee(eID int NOT NULL, name varchar(45) NOT NULL, startTime time, endTime time, PRIMARY KEY(eID))")
    mycursor.execute("create table Company(pID int NOT NULL, position varchar(45) NOT NULL, positionTaken char(3), directive text, PRIMARY KEY(pID));")
    mycursor.execute("create table PersonalInfo(eID int NOT NULL, pID int NOT NULL, yearlySalary int, email varchar(100), review text, FOREIGN KEY(eID) REFERENCES Employee(eID), FOREIGN KEY(pID) REFERENCES Company(pID))")
    mycursor.execute("insert into Employee values(1000, 'Christian Escobarete', '07:00:00', '15:00:00')")
    mycursor.execute("insert into Employee values(1001, 'Jillian Smith', '06:00:00', '14:00:00')")
    mycursor.execute("insert into Employee values(1002, 'Darcy Martinez', '07:00:00', '15:00:00')")
    mycursor.execute("insert into Employee values(1003, 'Luis Vazquez', '08:00:00', '16:00:00')")
    mycursor.execute("insert into Employee values(1004, 'Ada Lovelace', '08:00:00', '16:00:00')")
    mycursor.execute("insert into Company values(1, 'Developer', 'yes','Create a project that will change the world')")
    mycursor.execute("insert into Company values(2, 'Developer', 'yes','Create a porject that will change the world')")
    mycursor.execute("insert into Company values(3, 'Help Desk', 'yes','Answer the phone')")
    mycursor.execute("insert into Company values(4, 'Senior Devloper', 'yes','Create a porject that will chnage the world')")
    mycursor.execute("insert into Company values(5, 'Manager', 'yes','Manage the employees and make sure things get done')")
    mycursor.execute("insert into Company values(6, 'Developer', 'no', NULL)")
    mycursor.execute("insert into Company values(7, 'Information Technology', 'no', NULL)")
    mycursor.execute("insert into PersonalInfo values(1000, 1, 50000, 'cescobarete@business.com', 'A terrible employee')")
    mycursor.execute("insert into PersonalInfo values(1001, 5, 70000, 'jsmith@business.com', 'Exemplory employee')")
    mycursor.execute("insert into PersonalInfo values(1002, 3, 30000, 'dmartinez@business.com', 'Does not work well with others')")
    mycursor.execute("insert into PersonalInfo values(1003, 4, 80000, 'lvazquez@business.com', 'Smiles all the time')")
    mycursor.execute("insert into PersonalInfo values(1004, 2, 50000, 'alovelace@business.com', 'Sketchy')")
    con.commit
    mycursor.execute("CREATE INDEX Employee ON Employee(name, startTime, endTime)")
    mycursor.execute("CREATE USER ms_user@localhost IDENTIFIED BY 'manageuser'")
    mycursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON ManageEmp.* TO ms_user@localhost")
    con.commit()
    con.close()

def GetDisplay():
    os.system("python3 gui_display.py")

def UploadEmployee():
    os.system("python3 gui_employee.py")

def UploadCompany():
    os.system("python3 gui_company.py")

def UploadPersonalInfo():
    os.system("python3 gui_personalinfo.py")

root = Tk()

root.geometry("700x500")
root.title("Managment System: Main")

#executes employee gui table
openEmployee = Button(root, text='Employee Schedule       ', font=('italic',30), bg="white", command=UploadEmployee)
openEmployee.place(x=10, y=400)

#executes company gui table
openCompany = Button(root, text='Comapany Positions              ', font=('italic',30), bg="white", command=UploadCompany)
openCompany.place(x=325, y=400)

#executes personal inforamtion gui table
openPersonalInfo = Button(root, text='Personal Information              ', font=('italic',30), bg="white", command=UploadPersonalInfo)
openPersonalInfo.place(x=325, y=350)

#openData = Button(root, text='Open Database', font=('italic',10), bg="20bebe", command=threading.Thread(target=GetDisplay).start())
openData = Button(root, text='Database                           ', font=('italic',30), bg="white", command=GetDisplay)
openData.place(x=10, y=350)

root.mainloop()
