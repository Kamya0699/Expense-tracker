import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

class GraphWindow:
    def __init__(self):

        def expenseGraph():
            con=mysql.connector.connect(user="root", password="", host="localhost", database="expense tracker")
            sql="select expenseSource, expenseDate, amount from expenses group by expenseSource"
            servicedf=pd.read_sql(sql, con)
            print(servicedf)
            plt.title("expense amount vs source")
            plt.legend(labels=servicedf.expenseSource, loc="best")
            plt.pie(servicedf.amount, autopct='%.1f%%', labels=servicedf.expenseSource, shadow=True)

            plt.show()
            plt.savefig("expense.png")

        expenseGraph()

