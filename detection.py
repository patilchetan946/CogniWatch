import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
from keras.models import load_model
from tkinter import messagebox as ms
import CNNModel
import os

global fn
fn = ""

root = tk.Tk()
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Prediction")

# For background Image
image2 = Image.open('Background/Security.png')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Marquee text animation
def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if (x2 < 0 or y1 < 0):  # reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(500 // fps, shift)

canvas = tk.Canvas(root, bg="#000f22")
canvas.pack()
canvas.place(x=0, y=0)
text_var = "DETECT SUSPICIOUS ACTIVITY"
text = canvas.create_text(0, -2000, text=text_var, font=('Raleway', 25, 'bold'), fill='white', tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width'] = width
canvas['height'] = height
fps = 40  # Change the fps to make the animation faster/slower
shift()   # Function Calling

def update_label1(str_T):
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=600)
    image2 = Image.open('p2.jpg')
    image2 = image2.resize((w, h), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=200, y=200)

def update_cal(str_T):
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=400)

def train_model():
    update_label("Model Training Start...............")
    start = time.time()
    X = CNNModel.main()
    end = time.time()
    ET = "Execution Time: {0:.4} seconds \n".format(end-start)
    msg = "Model Training Completed.."+'\n'+ X + '\n'+ ET
    print(msg)

import functools
import operator

def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from tensorflow.keras.optimizers import Adam

    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH = 3
    print(fn)
    if fn != "":
        model = load_model('abnormalevent.h5')
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
        img = np.array(img)
        img = img.reshape(1, IMAGE_SIZE, IMAGE_SIZE, 3)
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:', img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        Nutrient = np.argmax(prediction)
        print(Nutrient)
        if Nutrient == 0:
            Cd = "Fighting"
        elif Nutrient == 1:
            Cd = "Accident"
        elif Nutrient == 2:
            Cd = "Robbery"
        elif Nutrient == 3:
            Cd = "Theft"
        elif Nutrient == 3:
            Cd = "Fraud"
        elif Nutrient == 3:
            Cd = "pre"
    A = Cd
    return A

def update_label(str_T):
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='pink', fg='black')
    result_label.place(x=300, y=450)

def test_model():
    global fn
    if fn != "":
        update_label("Model Testing Start...............")
        start = time.time()
        X = test_model_proc(fn)
        X1 = "{0} ".format(X)
        end = time.time()
        ET = "Execution Time: {0:.4} seconds \n".format(end-start)
        msg = "Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn = ""
    else:
        msg = "Please Select Image For Prediction...."
    update_label(msg)

def openimage():
    global fn
    fileName = askopenfilename(initialdir='SUSPICIOUS ACTIVITY DETECTION SYSTEM', title='Select image for Analysis ', filetypes=[("all files", "*.*")])
    IMAGE_SIZE = 200
    imgpath = fileName
    fn = fileName
    img = Image.open(imgpath)
    img = img.resize((IMAGE_SIZE, 200))
    img = np.array(img)
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)

def convert_grey():
    global fn
    IMAGE_SIZE = 200
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE, 200))
    img = np.array(img)
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])
    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)
    gs = cv2.resize(gs, (x1, y1))
    retval, threshold = cv2.threshold(gs,0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    img2 = tk.Label(root, image=imgtk, height=250, width=250, bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)
    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)
    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)

def close_labels():
    # Function to remove labels from the root window
    for label in root.grid_slaves():
        label.grid_forget()

def Fighting():
    close_labels()  # Remove existing labels
    label = tk.Label(root, text='''Suspicious human activities like fighting, shooting,
                   fire have got serious security concern in public places because 
                   of a steep surge in these types of cases all around. CCTV cameras 
                   are generally installed at public places like malls, railway stations; 
                   but evidences suggest that only availability of these cameras are not 
                   very effective unless the video feeds are constantly monitored. 
                   Therefore, we intend to build an automated and intelligent video 
                   surveillance system to detect the suspicious human activities, 
                   followed by an alert generation.
''', width=80, bg="white", fg="black", height=30)
    label.place(x=500, y=200)

def Accident():
    close_labels()  # Remove existing labels
    label = tk.Label(root, text='''Traveling is one of the basic needs of every 
                   person who lives in cities or villages. 
                   There are several ways to travel from one place to 
                   another by air, water, rail, and road in various types 
                   of vehicle, e.g., cars, motorbikes, buses, and trucks.
                   Roads are the foremost source of linking between cities 
                   and villages.

''', width=80, bg="white", fg="black", height=30)
    label.place(x=500, y=200)

def Robbery():
    close_labels()  # Remove existing labels
    label = tk.Label(root, text='''A major purpose of video surveillance
                   is the detection of unusual situations such as traffic 
                   accidents, robberies, or illicit activity.
                   The proposed system is concerned with the
                   development of a surveillance video framework 
                   in the residential area to detect any type of 
                   suspicious robbery activity.
''', width=80, bg="white", fg="black", height=30)
    label.place(x=500, y=200)

def FrameCon():
    close_labels()  # Remove existing labels
    # Frame for details
    frame_alpr = tk.LabelFrame(root, text=" Details ", width=400, height=300, bd=5, font=('times', 14, ' bold '),bg="pink",fg="black")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=600, y=250)

    # Function to upload video
    def uploadvedio():
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        cam = cv2.VideoCapture(filename)

        try:
            # creating a folder named data
            if not os.path.exists('data'):
                os.makedirs('data')
        # if not created then raise error
        except OSError:
            print ('Error: Creating directory of data')

        # frame
        currentframe = 0

        while(True):
            # reading from frame
            ret,frame = cam.read()

            if ret:
                # if video is still left continue creating images
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will show how many frames are created
                currentframe += 1
            else:
                break

        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()
        ms.showinfo("Message", "Successfully uploaded Video")

    def window():
        root.destroy()

    button4 = tk.Button(frame_alpr, text="Exit", command=window, width=12, height=1,font=('times 15 bold'),bd=0,bg="red", fg="white")
    button4.place(x=130, y=150)

    button3 = tk.Button(frame_alpr, text=" Upload Video ", command=uploadvedio,width=15, height=1, font=('times', 15, ' bold '),bg="GREEN",fg="white")
    button3.place(x=100, y=50)


def Fraud():
    close_labels()  # Remove existing labels
    label = tk.Label(root, text='''Fraud detection is a process to 
                   identify deceptive activities within an organization.
                   It deals with discovering any illegitimate actions as
                   early as possible, thus enabling a swift response and
                   minimization of damage.It combines machine learning 
                   with statistical models to identify suspicious patterns,
                   guaranteeing compliance and minimizing damage from
                   potential fraudulent activity.
''', width=80, bg="white", fg="black", height=30)
    label.place(x=500, y=200)

def pre():
    root.destroy()
    from subprocess import call
    call(['python', 'GUI_Master.py'])

def window():
    root.destroy()

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=250, height=580, bd=5, font=('times', 14, ' bold '), bg="white")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=235, y=140)

button1 = tk.Button(frame_alpr, text="Fighting", command=Fighting, width=18, height=2, font=('times', 15, ' bold '), bg="white", fg="black")
button1.place(x=10, y=10)

button2 = tk.Button(frame_alpr, text="Accident", command=Accident, width=18, height=2, font=('times', 15, ' bold '), bg="white", fg="black")
button2.place(x=10, y=90)

button3 = tk.Button(frame_alpr, text="Robbery", command=Robbery, width=18, height=2, font=('times', 15, ' bold '), bg="white", fg="black")
button3.place(x=10, y=170)

button4 = tk.Button(frame_alpr, text="FrameCon", command=FrameCon, width=18, height=2, bg="white", fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=250)

button4 = tk.Button(frame_alpr, text="Fraud", command=Fraud, width=18, height=2, bg="white", fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=330)

button5 = tk.Button(frame_alpr, text="Detection", command=pre, width=18, height=2, bg="Green", fg="white", font=('times', 15, ' bold '))
button5.place(x=10, y=410)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '), bg="Red", fg="white")
exit.place(x=25, y=490)

root.mainloop()
