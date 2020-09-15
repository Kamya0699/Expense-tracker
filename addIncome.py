from tkinter import *
import db.db
from tkinter import messagebox
import income.showIncome

class IncomeWindow:
    def __init__(self, data=''):
        self.data=data
        print(self.data)
        self.win=Tk()
        self.canvas = Canvas(self.win, width=600, height=400, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)

        # bringing the screen in the centre
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        strl = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

        # disable resize of the window

        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("WELCOME | Add income | ADMINISTRATOR")

    def add_frame(self):
        # create an inner frame
        self.frame = Frame(self.win, height=400, width=500)
        self.frame.place(x=55, y=50)
        x, y = 0, 0

        self.label = Label(self.frame, text="Add Income")
        self.label.config(font=("Courier", 30, 'bold'), bg='green yellow')
        self.label.place(x=120, y=y + 10)

        self.label=Label(self.frame, text="Add Income source")
        self.label.config(font=("Courier", 16, 'bold'),bg='White')
        self.label.place(x=x+10, y=90)
        self.inc=Entry(self.frame, font='Courier 16')
        self.inc.place(x=240, y=90)

        self.label = Label(self.frame, text="Add Income")
        self.label.config(font=("Courier", 16, 'bold'), bg='White')
        self.label.place(x=x + 10, y=140)
        self.des = Entry(self.frame, font='Courier 16')
        self.des.place(x=240, y=140)

        if self.data=='':
            self.button = Button(self.frame, text="SUBMIT", font=('helvetica', 20, 'underline italic'), bg='dark green',
                             fg='white', command=self.add_income)
            self.button.place(x=x + 80, y=y + 200)
        else:
            up=dict(self.data).get('values')
            # set the values in input boxes
            self.inc.insert(0, up[0])
            self.des.insert(0, up[1])
            self.button = Button(self.frame, text="UPDATE", font=('helvetica', 20, 'underline italic'), bg='dark green',
                                 fg='white', command=self.update_income)
            self.button.place(x=x + 80, y=y + 200)

        self.lblmsg=Label(self.frame, text='')
        self.lblmsg.config(font=('Courier', 12, 'bold'))
        self.lblmsg.place(x=x+100, y=y+260)

        self.win.mainloop()

    def add_income(self):
        data=( self.inc.get(),
               self.des.get()
        )
        if self.inc.get()=='':
            self.lblmsg.config(fg='red')
            self.lblmsg.config(text="please enter income source")

        elif self.des.get()=='':
            self.lblmsg.config(fg='red')
            self.lblmsg.config(text='please enter income')

        else:
            res=db.db.add_income(data)
            if res:
                self.lblmsg.config(fg='green')
                self.lblmsg.config(text="data added successfully")

            else:
                self.lblmsg.config(fg='red')
                self.lblmsg.config(text='Alert! please try again')

    def update_income(self):
        tup=(
            self.inc.get(),
            self.des.get(),
            dict(self.data).get('text')
        )
        res=db.db.update_income(tup)
        if res:
            messagebox.showinfo("Message","Income updated successfully")
            self.win.destroy()
            x=income.showIncome.showIncome()
            x.add_frame()

if __name__ == "__main__":
    x = IncomeWindow()
    x.add_frame()
