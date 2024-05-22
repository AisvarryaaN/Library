from tkinter import*
from tkinter import messagebox
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
mycursor =mydb.cursor()
def bookregister():
    
    bid = label_1_entry.get()
    title = label_2_entry.get()
    author = label_3_entry.get()
    status = label_4_entry.get()
    status = status.lower()
    dept = label_5_entry.get()
    if (bid ==""or title==""or author==""or status=="" or dept==""):
        messagebox.showinfo('Error', "Empty data cant be inserted")
    else:
        insertbooks = "insert into books values('" + bid +"','"+title+"','"+author+"','"+status+"','"+dept+"')"
    try:
        mycursor.execute(insertbooks)
        mydb.commit()
        messagebox.showinfo('Success',"Book added successfully")
        import menu
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
def addBook():
    global label_1_entry, label_2_entry, label_3_entry, label_4_entry,label_5_entry, mydb, mycursor, books, root
  
#BACKGROUND IMAGE
root=Tk()
root.title("Add Book")
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
#LABELS:
login_label = Label(root, text="ADD BOOKS", bg='black', fg="gold", font=("Courier",20,'bold'))
login_label.place(x=260,y=10)

label_1=Label(root,text="BOOK ID",bg='black', fg='gold', font=('Courier',13,'bold'))
label_1.place(x=60,y=80)
label_2=Label(root,text="TITLE",bg='black', fg='gold', font=('Courier',13,'bold'))
label_2.place(x=60,y=130)
label_3=Label(root,text="AUTHOR",bg='black', fg='gold', font=('Courier',13,'bold'))
label_3.place(x=60,y=180)
label_4=Label(root,text="STATUS(Avail or Issued)",bg='black', fg='gold', font=('Courier',13,'bold'))
label_4.place(x=60,y=230)
label_5=Label(root,text="DEPARTMENT",bg='black', fg='gold', font=('Courier',13,'bold'))
label_5.place(x=60,y=280)


label_1_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',13))
label_1_entry.place(x=380,y=80)
label_2_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',13))
label_2_entry.place(x=380,y=130)
label_3_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',13))
label_3_entry.place(x=380,y=180)
label_4_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',13))
label_4_entry.place(x=380,y=230)
label_5_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',13))
label_5_entry.place(x=380,y=280)
##############################################################################################
submit=Button(root,text="SUBMIT",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=bookregister)
submit.place(x=200,y=340)
def menupage():
    root.destroy()
    import menu1
quit1=Button(root,text="BACK",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=menupage)
quit1.place(x=400,y=340)
root.mainloop()
