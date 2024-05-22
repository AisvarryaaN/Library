from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor = mydb.cursor()
#BACKGROUND IMAGE
root=Tk()
root.title("View Book")
photo=PhotoImage(file="5.gif")
w=Label(root,image=photo)
w.pack()
root.geometry("700x410")
root.resizable(False,False)
#############################################################################################
#ICON IMAGE
image_icon=PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)
#############################################################################################
#LABELS
login_label = Label(root, text="EEE BOOKS", bg='black', fg="gold", font=("Courier",20,'bold'))
login_label.place(x=260,y=50)
Label(root, text="%-10s%-25s%-25s%-20s%-10s"%('BID','TITLE','AUTHOR','STATUS','DEPT'),bg='black',fg='gold',font=("Courier",10,'bold')).place(x=5,y=100)
sql = "select * from books where dept='eee'"
mycursor.execute(sql)
results=mycursor.fetchall()
for row in results:
    bid=row[0]
    title=row[1]
    author=row[2]
    status=row[3]
    dept=row[4]
    Label(root,text="%-10s%-25s%-25s%-20s%-10s"%(row[0],row[1],row[2],row[3],row[4]) ,bg='black', fg='gold',font=("Courier",10,'bold')).place(x=10,y=140)
    print("bid= %s,title= %s,author= %s,status= %s,dept= %s"%(bid,title,author,status,dept))
##############################################################################################
def menupage():
    root.destroy()
    import menu1
quit1=Button(root,text="BACK TO MENU",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=menupage)
quit1.place(x=270,y=340)
