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
def deptpage():
    root.destroy()
    import departments
view=Button(root, text="DEPARTMENTS", bg='black', fg="gold", font=("Courier",20,'bold'),activebackground="gold",activeforeground="black",command=deptpage)
view.place(x=260,y=150)

##############################################################################################


