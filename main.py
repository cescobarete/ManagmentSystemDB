import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
import os

def open_manage():
    os.system('python3 login-system.py')

def open_employee():
    os.system('python3 personal-login-system.py')

root = tk.Tk()
root.title('Desktop App')
root.resizable(False,False)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo2 = Image.open('logo2.png')
logo2 = logo2.resize((100,700), Image.ANTIALIAS)
logo2 = ImageTk.PhotoImage(logo2)
logo_label2 = tk.Label(image=logo2)
logo_label2.image = logo2
logo_label2.place(x=0,y=0)

logo3 = Image.open('logo2.png')
logo3 = logo3.resize((100,700), Image.ANTIALIAS)
logo3 = ImageTk.PhotoImage(logo3)
logo_label3 = tk.Label(image=logo3)
logo_label3.image = logo3
logo_label3.place(x=500,y=0)

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

openUser = tk.Button(root, text="Personal Information", font=('italic',20), highlightbackground='#3E4149', command=open_employee)
openUser.place(x=130,y=200)

openManage = tk.Button(root, text="Management", font=('italic',20), highlightbackground='#3E4149', command=open_manage)
openManage.place(x=330,y=200)

root.mainloop()