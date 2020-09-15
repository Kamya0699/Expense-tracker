from tkinter import *
from PIL import ImageTk, Image
import ExpenseTracker1

class WelcomeWindow:

    def __init__(self):
        self.win=Tk()
         # making the window screen
        self.canvas = Canvas(self.win, width=600, height=400, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)

        #bringing the screen in the centre
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        strl = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

       # disable resize of the window

        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("WELCOME | Expense Tracker | ADMINISTRATOR")

    def add_frame(self):
        # create an inner frame
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=75, y=50)
        x, y = 0, 0

    #  place the photo in the frame
        self.img = ImageTk.PhotoImage(Image.open("images/expense.jpg"))
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+10, y=y + 0)

        self.label = Label(self.frame, text="Welcome to expense tracker")
        self.label.config(font=("Courier", 20, 'bold'),bg='lightGreen')
        self.label.place(x=18, y=y + 10)

        self.button=Button(self.frame,text="Continue",font=('helvetica',20,'underline italic'),bg='dark green',fg='white', command=self.login)
        self.button.place(x=x+80, y=y+100)
        self.win.mainloop()
    # open a new window on pressing button
    def login(self):
        print("working")

        #destroy the current window frame
        self.win.destroy()
        # open the new login window
        log=ExpenseTracker1.LoginWindow()
        log.add_frame()

if __name__ == "__main__":
    x=WelcomeWindow()
    x.add_frame()