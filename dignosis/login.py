from Tkinter import *
import PIL
from PIL import Image,ImageTk
import mysql.connector
import tkMessageBox

def signup():
    root.destroy()
    import signup

def symptoms():
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="project")
    cursor=conn.cursor()
    cursor.execute("select * from login where username='"+e1.get()+"' and password='"+e2.get()+"'")
    if(cursor.fetchone()):
         root.destroy()
         import symptoms
        
    else:
        tkMessageBox.showinfo("Alert","Username or Password is wrong")
   

root=Tk()
root.title("Login")
root.geometry("1000x600+200+50")
root.resizable(width=False,height=False)

load=Image.open("ls.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

l1=Label(root,text="IF YOU ARE A NEW USER",fg="black",font=("times new roman",15))
l1.place(x=600,y=50)

b1=Button(root,text="SIGNUP",command=signup,font=("times new roman",11,"bold","underline"),relief="flat")
b1.place(x=835,y=49)

l2=Label(root,text="Username",fg="dark blue",font=("times new roman",20))
l2.place(x=70,y=150)

l3=Label(root,text="Password",fg="dark blue",font=("times new roman",20))
l3.place(x=70,y=250)

e1=Entry(root,bd=5,font=(20),justify=RIGHT)
e1.place(x=230,y=150)

e2=Entry(root,bd=5,font=(20),justify=RIGHT,show="*")
e2.place(x=230,y=250)

b2=Button(root,command=symptoms,text="Submit",bd=5,font=("times new roman",20),relief="solid",borderwidth=5)
b2.place(x=200,y=350)

l4=Label(root,text="BRINGING EXCELLENCE HOME",font=("algerian",20))
l4.place(x=100,y=500)

load2=Image.open("im.png")
render2=ImageTk.PhotoImage(load2)
img2=Label(root,image=render2)
img2.place(x=600,y=150)

load1=Image.open("download.png")
render1=ImageTk.PhotoImage(load1)
img1=Label(root,image=render1)
img1.place(x=10,y=10)


root.mainloop()

