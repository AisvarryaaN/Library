from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor = mydb.cursor()
#BACKGROUND IMAGE
root=Tk()
root.title("Department page")
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
def csepage():
    root.destroy()
    import cse
btn1 = Button(root,text="CSE DEPT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=csepage)
btn1.place(x=90,y=90)

def itpage():
    root.destroy()
    import it
btn2 = Button(root,text="IT DEPT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=itpage)
btn2.place(x=420,y=90)

def ecepage():
    root.destroy()
    import ece
btn3 = Button(root,text="ECE DEPT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=ecepage)
btn3.place(x=90,y=170)

def eeepage():
    root.destroy()
    import eee   
btn4 = Button(root,text="EEE DEPT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=eeepage)
btn4.place(x=420,y=170)

def eipage():
    root.destroy()
    import ei 
btn5 = Button(root,text="E&I DEPT",bg='black', fg='gold',font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=eipage)
btn5.place(x=250,y=250)

root.mainloop()
