from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter import *
from math import*
################################################################################
def deletebk():
    bid = label_1_entry.get()
    mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
    mycursor = mydb.cursor()
    try:
        mycursor.execute("select bid from books where bid='"+bid+"'")
        myresult=mycursor.fetchall()
        myresult[0]
        try:
            sql="delete from books where bid='"+(str(bid))+"'";
            mycursor.execute(sql)
            mydb.commit()
            print("Book ID deleted successfully")
            messagebox.showinfo('Success',"Book Record Deleted Successfully")
            root.destroy()
        except:
            mydb.rollback()
    except:
        print("Book ID doesn't exist")
        messagebox.showinfo('Error',"Book with given ID doesn't exist")
        root.destroy()
#BACKGROUND IMAGE
def delbook():
    global label_1_entry
root=Tk()
root.title("Delete Book")
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
login_label = Label(root, text="DELETE BOOK", bg='black', fg="gold", font=("Courier",20,'bold'))
login_label.place(x=260,y=50)
label_1=Label(root,text="BOOK ID",bg="black" ,fg='gold', font=('Courier',15,'bold'))
label_1.place(x=150,y=200)
label_1_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',15))
label_1_entry.place(x=340,y=200)
##############################################################################################
#BUTTONS
submit=Button(root,text="SUBMIT",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=deletebk)
submit.place(x=200,y=340)
def menupage():
    root.destroy()
    import menu1
quit1=Button(root,text="QUIT",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=menupage)
quit1.place(x=400,y=340)

