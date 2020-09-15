from tkinter import *
from PIL import ImageTk, Image
import income.addIncome
import income.showIncome
import expense.addexpense
import expense.showExpense
import graph.graph
import expense.expenseReg

class DashboardWindow:
    def __init__(self):
        self.win=Tk()

        self.canvas=Canvas(self.win, width=900, height=500, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-900/2)
        y=int(height/2-500/2)
        strl="900x500+" + str(x) + "+" + str(y)
        self.win.geometry(strl)

        self.win.resizable(width=FALSE, height=FALSE)
        self.win.title("WELCOME | Dashboard | ADMINISTRATOR")

    def add_menu(self):
        self.frame=Frame(self.win, height=700, width=900)
        self.frame.place(x=20, y=10)
        x, y =5, 5
        self.img = ImageTk.PhotoImage(Image.open("images/expense1.jpg"))
        self.label=Label(self.frame, image=self.img)
        self.label.place(x=x+0, y=y+0)

        self.menubar = Menu(self.win)

        self.incomemenu=Menu(self.menubar, tearoff=0)
        self.incomemenu.add_command(label="Add Income source", command=self.add_income)
        self.incomemenu.add_command(label="Manage Income Source", command=self.show_income)
        self.menubar.add_cascade(label="Income", menu=self.incomemenu)

        self.expensemenu = Menu(self.menubar, tearoff=0)
        self.expensemenu.add_command(label="Add Expenses", command=self.add_expense)
        self.expensemenu.add_command(label="Manage Expenses", command=self.show_expense)

        self.expensemenu.add_separator()
        self.expensemenu.add_command(label="Exit", command=self.win.quit)

        self.menubar.add_cascade(label="Expense", menu=self.expensemenu)


        self.graphmenu = Menu(self.menubar, tearoff=0)
        self.graphmenu.add_command(label="Show Graph", command=self.show_graph)
        self.menubar.add_cascade(label="Graph", menu=self.graphmenu)
        self.regmenu = Menu(self.menubar, tearoff=0)
        self.regmenu.add_command(label="Show Regression", command=self.show_regression)
        self.menubar.add_cascade(label="Regression", menu=self.regmenu)

        self.win.config(menu=self.menubar)
        self.win.mainloop()

    def add_income(self):
        x=income.addIncome.IncomeWindow()
        x.add_frame()
    def show_income(self):
        x=income.showIncome.showIncome()
        x.add_frame()
    def add_expense(self):
        x=expense.addexpense.ExpenseWindow()
        x.add_frame()
    def show_expense(self):
        x=expense.showExpense.showExpense()
        x.add_frame()
    def show_graph(self):
        x=graph.graph.GraphWindow()
        x.__init__()
    def show_regression(self):
        x=expense.expenseReg.Regression()
        x.__init__()
        x.predictions

if __name__ == "__main__":
    x=DashboardWindow()
    x.add_menu()




