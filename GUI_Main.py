import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="#D15FEE")
# root.geometry("1300x700")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("COGNIWATCH")



# For background Image
image2 = Image.open('Background/Front2.png')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Create a label for displaying images
logo_label = tk.Label(root)
logo_label.pack()

#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(500//fps,shift)

canvas = tk.Canvas(root, bg="#010175")
canvas.pack()
canvas.place(x=0, y=0)
text_var="COGNIWATCH: ADVANCED SCENE ANALYSIS FOR THREAT DETECTION AND PUBLIC SAFETY"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 80
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])

def pre():
    from subprocess import call
    call(["python","detection.py"])



def window():
  root.destroy()

# Create a label for the welcome title
# welcome_label = tk.Label(root, text="Welcome to COGNIWATCH", font=('times', 24, 'bold'), bg="#D15FEE", fg="white")
# welcome_label.place(x=520, y=480)  # Adjusted the y coordinate to place it above the button frame

# Create a frame to act as a box behind the buttons with rounded corners
button_frame = tk.Frame(root, bg="white", bd=2)
button_frame.place(x=480, y=535, width=440, height=145)
button_frame.config(highlightthickness=0, borderwidth=5)  # Adjust border width

# Define a custom style for rounded corners
style = ttk.Style()
style.configure('Rounded.TButton',bg="yellow", background="#000f22", font=('times', 20, ' bold '), foreground="Black")

button1 = ttk.Button(button_frame, text="LOGIN", command=log, width=13, style='Rounded.TButton')
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = ttk.Button(button_frame, text="REGISTER", command=reg, width=13, style='Rounded.TButton')
button2.grid(row=0, column=1, padx=10, pady=10)

# button3 = ttk.Button(button_frame, text="DETECTION", command=pre, width=13, style='Rounded.TButton')
# button3.grid(row=1, column=0, padx=10, pady=10)

button4 = ttk.Button(button_frame, text="EXIT", command=window, width=13, style='Rounded.TButton')
button4.grid(row=1, padx=10, pady=10)
root.mainloop()