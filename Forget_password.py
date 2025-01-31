import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3

class ForgotPasswordApp:

    def open_login(self):
        import subprocess
        import tkinter as tk
        # Open the login script
        subprocess.Popen(["python", "login.py"])
        # Destroy the previous window
        self.root.destroy()

    def change_password(self):
        new_password_entry = self.password.get()
        confirm_password_entry = self.confirmPassword.get()

        if new_password_entry == "":
            ms.showerror('Error!', "Password cannot be empty")
            return

        if new_password_entry != confirm_password_entry:
            ms.showerror('Error!', "Passwords didn't match")
            return

        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        find_user = 'SELECT * FROM admin_registration WHERE Email=?'
        c.execute(find_user, [(str(self.email.get()))])

        result = c.fetchall()
        if result:
            db = sqlite3.connect('evaluation.db')
            curs = db.cursor()

            curs.execute("update admin_registration set password=? WHERE Email=? ", (str(new_password_entry), self.email.get()))
            db.commit()
            db.close()
            ms.showinfo('Congrats', 'Password changed successfully')
        else:
            ms.showerror('Error!', "Email not found in database")

    def __init__(self, root):
        self.root = root
        self.root.configure(background='white')
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.title("Forget Password")

        self.background_image = ImageTk.PhotoImage(Image.open("Background/ForgetPass3.png").resize((self.w, self.h), Image.LANCZOS))
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0)

        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirmPassword = tk.StringVar()

        self.frame = tk.Frame(root, bg="#FFDB4A")
        self.frame.place(x=540, y=425, height=200, width=370)

        tk.Label(root, text="Enter Email :", width=10, font=("Helvetica", 13, "bold"), bg="#FFDB4A", bd=0).place(x=550, y=440)
        tk.Label(root, text="New Password :", width=13, font=("Helvetica", 13, "bold"), bg="#FFDB4A", bd=0).place(x=550, y=490)
        tk.Label(root, text="Confirm Password :", width=15, font=("Helvetica", 13, "bold"), bg="#FFDB4A", bd=0).place(x=550, y=540)

        tk.Entry(root, textvariable=self.email).place(x=730, y=440, height=20, width=160)
        tk.Entry(root, textvariable=self.password).place(x=730, y=490, height=20, width=160)
        tk.Entry(root, textvariable=self.confirmPassword).place(x=730, y=540, height=20, width=160)
        tk.Button(root, text="Submit", font=("Helvetica", 13, "bold"), bg="#6237CF", fg="white", padx=16, pady=10, command=self.change_password).place(x=565, y=585, height=35, width=150)
        tk.Button(root, text="Login Now", font=("Helvetica", 13, "bold"), bg="#00BF63", fg="black", padx=16, pady=10, command=self.open_login).place(x=740, y=585, height=35, width=150)
def main():
    root = tk.Tk()
    app = ForgotPasswordApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
