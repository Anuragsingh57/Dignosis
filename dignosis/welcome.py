from Tkinter import *
#import PIL
#from PIL import Image,ImageTk

def login():
    root.destroy()
    import login

def signup():
    root.destroy()
    import signup

root=Tk()
root.title("WELCOME")
root.geometry("1000x550+200+50")
root.resizable(width=False,height=False)
'''
load=Image.open("welcome.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
'''
l=Label(root,text="WELCOME TO DISEASE PREDICTION,",width=50,bg="SteelBlue1",height=2,font=("times new roman",25,"bold"))
l.place(x=0,y=220)
l1=Label(root,text="MACHINE LEARNING AND HEALTH CARE",width=50,bg="SteelBlue1",height=2,font=("times new roman",25,"bold"))
l1.place(x=0,y=290)

b1=Button(root,command=login,text="LOGIN",bg="SteelBlue1",font=("times new roman",15,"bold","italic","underline"),relief="flat")
b1.place(x=750,y=50)
b2=Button(root,command=signup,text="SIGNUP",bg="SteelBlue1",font=("times new roman",15,"bold","italic","underline"),relief="flat")
b2.place(x=850,y=50)
'''
load1=Image.open("download.png")
render1=ImageTk.PhotoImage(load1)
img1=Label(root,image=render1)
img1.place(x=10,y=10)
'''
root.mainloop()
