import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="expense tracker")

cursor=con.cursor()


# make a function to access the database
def user_login(tup):
    try:
        cursor.execute("select * from 'expense' where 'username'=%s and 'password'=%s",tup)
        return cursor.fetchone()
    except:
        return False