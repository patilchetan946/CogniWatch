import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create labels with different fonts
label1 = tk.Label(root, text="Arial Font", font=("Arial", 12))
label1.pack()

label2 = tk.Label(root, text="Times New Roman Font", font=("Times New Roman", 12))
label2.pack()

label3 = tk.Label(root, text="Courier New Font", font=("Courier New", 12))
label3.pack()

label4 = tk.Label(root, text="Verdana Font", font=("Verdana", 12))
label4.pack()

label5 = tk.Label(root, text="Tahoma Font", font=("Tahoma", 12))
label5.pack()

label6 = tk.Label(root, text="Georgia Font", font=("Georgia", 12))
label6.pack()

label7 = tk.Label(root, text="Comic Sans MS Font", font=("Comic Sans MS", 12))
label7.pack()

label8 = tk.Label(root, text="Trebuchet MS Font", font=("Trebuchet MS", 12))
label8.pack()

label9 = tk.Label(root, text="Impact Font", font=("Impact", 12))
label9.pack()

label10 = tk.Label(root, text="Palatino Linotype Font", font=("Palatino Linotype", 12))
label10.pack()

root.mainloop()