from Tkinter import *
import PIL
from PIL import Image,ImageTk
import tkMessageBox
import mysql.connector

root=Tk()
root.title("Signup")
root.geometry("1000x600+200+50")
root.resizable(width=False,height=False)

load=Image.open("ls.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

def submit():
    if(e1.get()=="" or e2.get()=="" or e3.get()==""or e4.get()=="" or e5.get()=="" or e6.get()==""):
        tkMessageBox.showinfo("Alert","Please fill all the fields")

    elif(len(e6.get())<=6 or len(e6.get())>=12):
        tkMessageBox.showinfo("Alert","Password length is not correct")

    elif(e6.get()!= e7.get()):
        tkMessageBox.showinfo("Alert","password not matched")
    
    else:
        conn=mysql.connector.connect(user="root",password="",host="localhost",database="project")
        cursor=conn.cursor()
        cursor.execute("insert into login(name,age,gender,email,username,password) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get()+"','"+e6.get()+"')")
        conn.commit()
        root.destroy()
        import login


l1=Label(root,text="Name",fg="dark blue",font=("times new roman",20))
l1.place(x=150,y=150)

l2=Label(root,text="Age",fg="dark blue",font=("times new roman",20))
l2.place(x=150,y=200)

l3=Label(root,text="Gender",fg="dark blue",font=("times new roman",20))
l3.place(x=150,y=250)

l4=Label(root,text="Email-id",fg="dark blue",font=("times new roman",20))
l4.place(x=150,y=300)

l5=Label(root,text="Username",fg="dark blue",font=("times new roman",20))
l5.place(x=150,y=350)

l6=Label(root,text="Password",fg="dark blue",font=("times new roman",20))
l6.place(x=150,y=400)

l7=Label(root,text="Confirm Password",fg="dark blue",font=("times new roman",20))
l7.place(x=150,y=450)

e1=Entry(root,bd=5,font=(20),justify=RIGHT)
e1.place(x=400,y=150)

e2=Entry(root,bd=5,font=(20),justify=RIGHT)
e2.place(x=400,y=200)

e3=Entry(root,bd=5,font=(20),justify=RIGHT)
e3.place(x=400,y=250)

e4=Entry(root,bd=5,font=(20),justify=RIGHT)
e4.place(x=400,y=300)

e5=Entry(root,bd=5,font=(20),justify=RIGHT)
e5.place(x=400,y=350)

e6=Entry(root,bd=5,font=(20),justify=RIGHT,show="*")
e6.place(x=400,y=400)

e7=Entry(root,bd=5,font=(20),justify=RIGHT,show="*")
e7.place(x=400,y=450)


b1=Button(root,command=submit,text="Submit",bd=5,font=("times new roman",25),relief='solid',borderwidth=5)
b1.place(x=300,y=500)

load1=Image.open("download.png")
render1=ImageTk.PhotoImage(load1)
img1=Label(root,image=render1)
img1.place(x=10,y=10)

load2=Image.open("su.png")
render2=ImageTk.PhotoImage(load2)
img2=Label(root,image=render2)
img2.place(x=650,y=175)

root.mainloop()
