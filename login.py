import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3
import cv2
import threading

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()


def forget():
    from subprocess import call
    call(["python", "Forget_password.py"])


def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.withdraw()

def login():
    # Establish Connection
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

        # Find user If there is any take proper action
        find_entry = 'SELECT * FROM admin_registration WHERE username = ? and password = ?'
        c.execute(find_entry, (username.get(), password.get()))
        result = c.fetchall()

        if result:
            ms.showinfo("Message", "Login successful")
            root.withdraw()

            # Open GUI_master.py
            import subprocess
            subprocess.Popen(["python", "GUI_master.py"])

        else:
            ms.showerror('Error', 'Username or Password did not match')


# Background Image
image2 = Image.open('Background/login.png')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

title=tk.Label(root, text="Login Here", font=("Aerial", 20, "bold"),bd=5,bg="Red",fg="Yellow")
title.place(x=290,y=320,width=150)

# Login frame
Login_frame = tk.Frame(root, bg="white")
Login_frame.place(x=130, y=410)

lbluser = tk.Label(Login_frame, text="Username", compound=tk.LEFT, font=("Times new roman", 20, "bold"), bg="white")
lbluser.grid(row=1, column=0, padx=20, pady=10)
txtuser = tk.Entry(Login_frame, bd=5, textvariable=username, font=("", 15))
txtuser.grid(row=1, column=1, padx=20)

lblpass = tk.Label(Login_frame, text="Password", compound=tk.LEFT, font=("Times new roman", 20, "bold"), bg="white")
lblpass.grid(row=2, column=0, padx=50, pady=10)
txtpass = tk.Entry(Login_frame, bd=5, textvariable=password, show="*", font=("", 15))
txtpass.grid(row=2, column=1, padx=20)

btn_log = tk.Button(Login_frame, text="Login", command=login, width=15, font=("Times new roman", 14, "bold"), bg="Green", fg="black")
btn_log.grid(row=3, column=1, pady=10)
btn_reg = tk.Button(Login_frame, text="Create Account", command=registration, width=15, font=("Times new roman", 14, "bold"), bg="red", fg="black")
btn_reg.grid(row=3, column=0, pady=10)

forgetpassword_button = tk.Button(Login_frame, text="Forget Password ?", command=forget, font=("Times new roman", 14, "bold"), bg="white", fg="black", bd=0)
forgetpassword_button.grid(row=4, column=0, pady=10, columnspan=2, sticky="nsew")

root.mainloop()
