from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter import*
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor = mydb.cursor()
def returnbk():
    bid = label_1_entry.get()
    if (bid!=""):
        mycursor.execute("select status from books where bid=%d"%(int(bid)))
        myresult=mycursor.fetchone()
        c=int(myresult[0])
        c=c+1
        print("count=",c)
        mycursor.execute("update books set status='%s' where bid=%d"%(str(c),int(bid)))
        mydb.commit()
        messagebox.showinfo('Success',"Status updated successsfully")
        root.destroy()
    else:
        messagebox.showinfo('Eror',"Please enter the book ID")
    
#BACKGROUND IMAGE
root=Tk()
root.title("Return Book")
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
login_label = Label(root, text="RETURN BOOK", bg='black', fg="gold", font=("Courier",20,'bold'))
login_label.place(x=260,y=50)
label_1=Label(root,text="BOOK ID",bg='black', fg='gold', font=('Courier',15,'bold'))
label_1.place(x=150,y=200)
label_1_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',15))
label_1_entry.place(x=340,y=200)
##############################################################################################
#BUTTONS
submit=Button(root,text="RETURN",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=returnbk)
submit.place(x=200,y=340)
def menupage():
    root.destroy()
    import menu1
quit1=Button(root,text="QUIT",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=menupage)
quit1.place(x=400,y=340)
