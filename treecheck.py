from tkinter import *
from tkinter.ttk import *
import mysql.connector
root=Tk()
root.title("View book")
photo=PhotoImage(file="5.gif")
w=Label(root,image=photo)
w.pack()
root.geometry("800x410")
root.resizable(False,False)
image_icon=PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)
mydb=mysql.connector.connect(host='localhost',user='root',password='Aishu106#206$',database='library')
mycu=mydb.cursor()
root=LabelFrame(w,text="VIEW BOOKS")
root.pack(fill="both",expand="yes",padx=20,pady=10)
trv=Treeview(w,columns=(1,2,3,4),show="headings",height="10")
trv.pack()
trv.heading(1,text="BID")
trv.heading(2,text="TITLE")
trv.heading(3,text="AUTHOR")
trv.heading(4,text="STATUS")
mycu.execute("select * from books")
myresult=mycu.fetchall()
for i in myresult:
    trv.insert('','end',value=i)
def clear():
    select=trv.selection()[0]
    trv.delete(select)
b=Button(w,text="clear",command=clear)
b.pack()
    
