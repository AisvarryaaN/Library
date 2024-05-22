from tkinter import *
root=Tk()
photo=PhotoImage(file="3.gif")
w=Label(root,image=photo)
w.pack()
def mp():
    root.destroy()
    import menu
BM=Button(w,bg='black',fg='white',text="menu",bd=0,command=mp)
BM.place(x=100,y=100)
root.mainloop()
