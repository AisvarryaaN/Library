import mysql.connector
from tkinter import *
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor = mydb.cursor()
bid=1
mycursor.execute("select status from books where bid='%d'"%(bid))
myresult=mycursor.fetchone()
c=int(myresult[0])
c=c-1
mycursor.execute("update books set status='%s' where bid=%d"%(str(c),bid))
