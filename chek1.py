from tkinter import *
from tkinter.ttk import *
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
root.geometry("750x610")
root.resizable(False,False)
#############################################################################################
#ICON IMAGE
image_icon=PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)
#############################################################################################
#LABELS
root=LabelFrame(w,text="VIEW BOOKS")
root.pack(fill="both",expand="yes",padx=20,pady=10)
trv=Treeview(w,columns=(1,2,3,4),show="headings",height="10")
trv.pack()
trv.heading(1,text="BID")
trv.heading(2,text="TITLE")
trv.heading(3,text="AUTHOR")
trv.heading(4,text="STATUS")
mycursor.execute("select * from books where dept='cse'")
myresult=mycursor.fetchall()
for i in myresult:
    trv.insert('','end',value=i)
def menupage():
    root.destroy()
    import menu1
b=Button(w,text="BACK TO MENU",command=menupage)
b.pack()
    
##############################################################################################


'''
quit1=Button(root,text="BACK TO MENU",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=menupage)
quit1.place(x=270,y=340)

'''
