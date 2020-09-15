from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import db.db
import expense.showExpense

class ExpenseWindow:
    def __init__(self,data=''):
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
        self.win.title("WELCOME | Add Expense | ADMINISTRATOR")

    def add_frame(self):
        # create an inner frame
        self.frame = Frame(self.win, height=400, width=500)
        self.frame.place(x=55, y=50)
        x, y = 0, 0
        self.label = Label(self.frame, text="Add Expense")
        self.label.config(font=("Courier", 25, 'bold'), bg='green yellow')
        self.label.place(x=120, y=y + 10)
        # drop down menu
        OPTIONS=[
            'Food',
            'Petrol',
            'Shopping',
            'Entertainment',
            'College'
        ]
        self.variable=StringVar(self.win)
        self.variable.set(OPTIONS[0])

        self.label = Label(self.frame, text="Add Expense Source")
        self.label.config(font=("Courier", 15, 'bold'))
        self.label.place(x=x+10, y=90)
        self.source=OptionMenu(self.frame, self.variable, *OPTIONS, command=self.dropdown)
        self.source.place(x=250, y=90)

        self.label = Label(self.frame, text="Add amount")
        self.label.config(font=("Courier", 15, 'bold'))
        self.label.place(x=x + 10, y=120)
        self.inc = Entry(self.frame, font='Courier 16')
        self.inc.place(x=250, y=120)

        # calendar
        self.label = Label(self.frame, text="Add date")
        self.label.config(font=("Courier", 15, 'bold'))
        self.label.place(x=x + 10, y=150)
        self.dob=DateEntry(self.frame, font=('Courier',12,'bold'),bg='darkblue',fg='white', borderwidth=2, command=self.dates,
                           date_pattern='YYYY/MM/DD')
        self.dob.place(x=250, y=150)

        # on date change listener
        self.dob.bind('<<DateEntrySelected>>', self.dates)

        if self.data=='':
            self.button = Button(self.frame, text="SUBMIT", font=('helvetica', 20, 'underline italic'), bg='dark green',
                             fg='white', command=self.add_expense)
            self.button.place(x=x + 80, y=y + 200)
        else:
            up=dict(self.data).get('values')
            # set the values in input boxes

            self.inc.insert(0, up[1])
            self.dob.insert(0,up[2])
            self.button = Button(self.frame, text="UPDATE", font=('helvetica', 20, 'underline italic'), bg='dark green',
                                 fg='white', command=self.update_expense)
            self.button.place(x=x + 80, y=y + 200)

        self.lblmsg = Label(self.frame, text='')
        self.lblmsg.config(font=('Courier', 12, 'bold'))
        self.lblmsg.place(x=x + 100, y=y + 260)

        self.win.mainloop()

    def dropdown(self,value,*args):
        print(self.variable.get())
    def dates(self, value, *args):
        print(self.dob.get_date())

    def add_expense(self):
        data = (self.variable.get(),
                self.inc.get(),
                self.dob.get()
                )
        if self.variable.get() == '':
            self.lblmsg.config(fg='red')
            self.lblmsg.config(text="please enter expense source")

        elif self.inc.get() == '':
            self.lblmsg.config(fg='red')
            self.lblmsg.config(text='please enter amount')

        elif self.dob.get() == '':
            self.lblmsg.config(fg='red')
            self.lblmsg.config(text='please enter date')

        else:
            res = db.db.add_expense(data)
            if res:
                self.lblmsg.config(fg='green')
                self.lblmsg.config(text="data added successfully")

            else:
                self.lblmsg.config(fg='red')
                self.lblmsg.config(text='Alert! please try again')

    def update_expense(self):
        tup=(
            self.inc.get(),
            self.dob.get(),
            dict(self.data).get('text')
        )
        res=db.db.update_expense(tup)
        if res:
            messagebox.showinfo("Message","expense updated successfully")
            self.win.destroy()
            x=expense.showExpense.showExpense()
            x.add_frame()

if __name__=="__main__":
    x=ExpenseWindow()
    x.add_frame()