from tkinter import*
from tkinter import messagebox
import mysql.connector
bid = 3
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
cursor = mydb.cursor()
sql="select bid from books where bid='%d'"%(bid)
cursor.execute(sql)
result=cursor.fetchall()
n=(str(*result[0]))
print(n)
if(n==bid):
    try:
        sql = "delete from books where bid='%d'"%(bid);
        cursor.execute(sql)
        mydb.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo('Error',"Book with given ID doesn't exist")

