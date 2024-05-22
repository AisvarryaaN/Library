from tkinter import*
from tkinter import messagebox
import mysql.connector
db = mysql.connector.connect(host ="localhost",user = "root",password = "Aishu106#206$",database="library")
cursor = db.cursor()
#BACKGROUND IMAGE
root=Tk()
root.title("Login page")
photo=PhotoImage(file="3.gif")
w=Label(root,image=photo)
w.pack()
root.geometry("700x410")
root.resizable(False,False)
#############################################################################################
#ICON IMAGE
image_icon=PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)
#############################################################################################
#Username and password:

login_label = Label(root, text="LIBRARY MANAGEMENT SYSTEM", bg='black', fg="gold", font=("Courier",25,'bold'))
login_label.place(x=100,y=50)
username=Label(root,text="USERNAME",bg='black', fg='gold', font=('Courier',15,'bold'))
username.place(x=150,y=150)
password=Label(root,text="PASSWORD",bg='black', fg='gold', font=('Courier',15,'bold'))
password.place(x=150,y=200)

username_entry=Entry(root,width=20,bg='black', fg='gold',font=('Courier',15))
username_entry.place(x=350,y=150)
password_entry=Entry(root,width=20,bg='black',show="*", fg='gold',font=('Courier',15))
password_entry.place(x=350,y=200)
#################################################################################################
#LOGIN BUTTON:
def login():
    username = "aishu"
    password = "aishu123"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        root.destroy()
        import menu
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
login=Button(root,text="LOGIN",bg='black',fg='gold', font=('Courier',15,'bold'),activebackground="gold",activeforeground="black",command=login)
login.place(x=320,y=250)
##################################################################################################
#EYE IMAGE OPEN AND CLOSE
button_mode=True
def hide():
    global button_mode
    
    if button_mode:
        eyebutton.config(image=closeeye,activebackground="gold")
        password_entry.config(show="*")
        button_mode=False
        
    else:
        eyebutton.config(image=openeye,activebackground="gold")
        password_entry.config(show="")
        button_mode=True
        
closeeye=PhotoImage(file="closeeye.gif")
openeye=PhotoImage(file="openeye.gif")
eyebutton=Button(root,image=openeye,bg='gold',fg='gold',bd=0,command=hide)
eyebutton.place(x=600,y=200)

root.mainloop()

