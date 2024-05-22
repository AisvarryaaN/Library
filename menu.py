from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter import *
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor = mydb.cursor()
#BACKGROUND IMAGE
root=Tk()
root.title("Menu page")
photo=PhotoImage(file="5.gif")
w=Label(root,image=photo)
w.pack()
root.geometry("700x410")
root.resizable(False,False)
#############################################################
#ICON IMAGE
image_icon=PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)
##############################################################
#ITEM TO BE DISPLAYED
def addpage():
    root.destroy()
    import add
btn1 = Button(root,text="ADD BOOKS",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=addpage)
btn1.place(x=90,y=90)

def deletepage():
    root.destroy()
    import delete
btn2 = Button(root,text="DELETE BOOKS",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=deletepage)
btn2.place(x=420,y=90)

def viewpage():
    root.destroy()
    import view
btn3 = Button(root,text="VIEW BOOKS",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=viewpage)
btn3.place(x=90,y=170)

def issuepage():
    root.destroy()
    import issue   
btn4 = Button(root,text="ISSUED BOOKS",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=issuepage)
btn4.place(x=420,y=170)

def returnpage():
    root.destroy()
    import Return   
btn5 = Button(root,text="RETURN  BOOKS",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=returnpage)
btn5.place(x=250,y=250)

def homepage():
    root.destroy()
    import loginpage   
btn6 = Button(root,text="LOGOUT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=homepage)
btn6.place(x=300,y=350)


root.mainloop()
