from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import db.db
import dashboard

class LoginWindow:
    def __init__(self):
        self.win=Tk()
        self.canvas=Canvas(self.win, width=600, height=500, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-500/2)
        strl="600x500+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

        self.win.resizable(width=FALSE, height=FALSE)
        self.win.title("WELCOME | Login Window | ADMINISTRATOR")

    def add_frame(self):
        self.frame=Frame(self.win, height=600, width=500)
        self.frame.place(x=56, y=60)
        x, y =5, 5
        self.img = ImageTk.PhotoImage(Image.open("images/login.jpg"))
        self.label=Label(self.frame, image=self.img)
        self.label.place(x=x+0, y=y+0)

        # login form creation
        self.label=Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y=y+150)

        self.uslabel=Label(self.frame, text='Enter username')
        self.uslabel.config(font=("Courier", 15, 'bold'))
        self.uslabel.place(x=10, y=y + 250)
        self.username=Entry(self.frame, font="courier 15")
        self.username.place(x=250,y=y+250)

        self.pslabel = Label(self.frame, text='Enter password')
        self.pslabel.config(font=("Courier", 15, 'bold'))
        self.pslabel.place(x=10, y=y + 300)
        self.password = Entry(self.frame,show="*",  font="courier 15")
        self.password.place(x=250, y=y + 300)

        self.button = Button(self.frame, text="Login", font=('helvetica', 20, 'underline italic'), bg='Dark Blue',
                             fg='white', command=self.login)
        self.button.place(x=x + 10, y=y + 350)

        self.win.mainloop()

    def login(self):
        #get the data

        self.u = self.username.get()
        self.v = self.password.get()

        #validations
        if self.username.get()=="":
            messagebox.showinfo("Alert!"," enter username first.")
        elif self.password.get()=="":
            messagebox.showinfo("Alert!", "enter password first.")
        else:
            res = db.db.user_login(self.u, self.v)
            if res == None:
                messagebox.showinfo("Alert!", "Invalid username/password")

            else:
                messagebox.showinfo("Message", "login successful!!")
                self.win.destroy()
                x=dashboard.DashboardWindow()
                x.add_menu()





