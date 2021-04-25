import tkinter as tk

import PyPDF2
from PIL import Image, ImageTk

import os

import mysql.connector as mysql
from mysql.connector import errorcode

def open_manage():
    os.system('python3 login-system.py')

def open_employee():
    os.system('python3 personal-login-system.py')

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#def executeScript(managmentDatabase):
    #fd = open(managmentDatabase, 'r')
    #sqlfile = fd.read()
    #fd.close()
    #sqlCommands = sqlfile.split(';')

    #for command in sqlCommands:

        #if command.strip() != '':
            #cursor.execute(command)

#executeScript('managmentDatabase.sql')
#con.commit()

root = tk.Tk()
root.title('Desktop App')
root.config(bg='white')
root.resizable(False,False)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo2 = Image.open('boss.png')
logo2 = logo2.resize((65,65), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(logo2)
logo_label2 = tk.Label(image=logo2)
logo_label2.image = logo2
logo_label2.place(x=270,y=220)

logo3 = Image.open('personel.png')
logo3 = ImageTk.PhotoImage(logo3)
logo_label3 = tk.Label(image=logo3)
logo_label3.image = logo3
logo_label3.place(x=-70,y=150)

logo = Image.open('design.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(x=200,y=0)

openUser = tk.Button(root, text="Personal Information", font=('italic',20), highlightbackground='#3E4149', command=open_employee)
openUser.place(x=50,y=240)

openManage = tk.Button(root, text="Management", font=('italic',20), highlightbackground='#3E4149', command=open_manage)
openManage.place(x=330,y=240)

root.mainloop()