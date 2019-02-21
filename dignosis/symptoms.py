from Tkinter import *
import ttk
import PIL
from PIL import Image,ImageTk
import pandas
import csv
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import mysql.connector
import tkMessageBox

def upload():
    table='symptoms'
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="project")
    cursor=conn.cursor()
    qu='SELECT * FROM %s ORDER BY id DESC LIMIT 2;'%table
    cursor.execute(qu)
    with open('fill','w')as f:
        writer=csv.writer(f)
        for row in cursor.fetchall():
            writer.writerow(row)

    file2=genfromtxt("fill",delimiter=',',dtype='int')
    file1=genfromtxt("ds.csv",delimiter=',',dtype='str')

    dic={}
    count=0
    for val in file1:
        if val[11] not in dic:
            dic[val[11]]=count
            count+=1
    for val in file1:
        val[11]=dic[val[11]]
    trainingSet=file1
    testingSet=file2

    trainingX=trainingSet[:,[0,1,2,3,4,5,6,7,8,9,10]]
    trainingX=trainingX.astype(float)
    trainingY=trainingSet[:,[11]]

    testingX=testingSet[:,[1,2,3,4,5,6,7,8,9,10,11]]
    #testingX=testingX.astype(float)

    lr=linear_model.LogisticRegression()
    lr.fit(trainingX,trainingY)

    a=int(lr.predict([testingX[1]]))
    for x in dic:
        if(dic[x]==a):
            res1.set("you might be suffering from %s"%x)

    
def  symptoms():
    conn=mysql.connector.connect(user="root",password="",host="localhost",database="project")
    cursor=conn.cursor()
    if(v1.get()=="Sore throat"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(sore_throat) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(sore_throat) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(sore_throat) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
 
    elif(v1.get()=="Fever"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(fever) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(fever) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(fever) values(3)")
            con.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
            
    elif(v1.get()=="swelling of body"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(swelling_of_body) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(swelling_of_body) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(swelling_of_body) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Dizziness"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(dizziness) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(dizziness) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(dizziness) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Head ache"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(headache) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(headache) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(headache) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Body ache"):
        if(l1.get()=="low"):          
            cursor.execute("insert into symptoms(bodyache) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(bodyache) values(2)")
            conn.commit()
        elif(l1.get()=="high"):            
            cursor.execute("insert into symptoms(bodyache) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Rash"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(rash) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(rash) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(rash) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Fatigue"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(fatigue) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(fatigue) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(fatigue) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Chills"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(chills) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(chills) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(chills) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Muscle ache"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(muscleache) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(muscleache) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(muscleache) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v1.get()=="Coughing"):
        if(l1.get()=="low"):
            cursor.execute("insert into symptoms(coughing) values(1)")
            conn.commit()
        elif(l1.get()=="mild"):
            cursor.execute("insert into symptoms(coughing) values(2)")
            conn.commit()
        elif(l1.get()=="high"):
            cursor.execute("insert into symptoms(coughing) values(3)")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        cursor.execute("insert into symptoms(sore_throat,fever,swelling_of_body,dizziness,headache,bodyache,rash,fatigue,chills,muscleache,coughing) values(0,0,0,0,0,0,0,0,0,0,0)")
        conn.commit()
        
        
    if(v2.get()=="Sore throat"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Fever"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="swelling of body"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Dizziness"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Head ache"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Body ache"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Rash"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Fatigue"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Chills"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Muscle ache"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v2.get()=="Coughing"):
        if(l2.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l2.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l2.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
    else:
        print ("not inserted")
        
    if(v3.get()=="Sore throat"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l3get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Fever"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="swelling of body"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Dizziness"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Head ache"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Body ache"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Rash"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Fatigue"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
    elif(v3.get()=="Chills"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Muscle ache"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v3.get()=="Coughing"):
        if(l3.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l3.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l3.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v4.get()=="Sore throat"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Fever"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="swelling of body"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Dizziness"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Head ache"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Body ache"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Rash"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Fatigue"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Chills"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Muscle ache"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v4.get()=="Coughing"):
        if(l4.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l4.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l4.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v5.get()=="Sore throat"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()        
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Fever"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="swelling of body"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Dizziness"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Head ache"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Body ache"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Rash"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Fatigue"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Chills"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Muscle ache"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()        
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v5.get()=="Coughing"):
        if(l5.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l5.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l5.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v6.get()=="Sore throat"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Fever"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="swelling of body"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Dizziness"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Head ache"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Body ache"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Rash"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Fatigue"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Chills"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Muscle ache"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v6.get()=="Coughing"):
        if(l6.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l6.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l6.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v7.get()=="Sore throat"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Fever"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()        
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="swelling of body"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Dizziness"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Head ache"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Body ache"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
    elif(v7.get()=="Rash"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Fatigue"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Chills"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Muscle ache"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v7.get()=="Coughing"):
        if(l7.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l7.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l7.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v8.get()=="Sore throat"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Fever"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="swelling of body"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Dizziness"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Head ache"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Body ache"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Rash"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Fatigue"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Chills"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Muscle ache"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v8.get()=="Coughing"):
        if(l8.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l8.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l8.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v9.get()=="Sore throat"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Fever"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="swelling of body"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Dizziness"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Head ache"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Body ache"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Rash"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Fatigue"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Chills"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v9.get()=="Muscle ache"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
    elif(v9.get()=="Coughing"):
        if(l9.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l9.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l9.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v10.get()=="Sore throat"):
        if(l10.get()=="low"):    
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="Fever"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="swelling of body"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
    elif(v10.get()=="Dizziness"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="Head ache"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
    elif(v10.get()=="Body ache"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
    elif(v10.get()=="Rash"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
    elif(v10.get()=="Fatigue"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="Chills"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="Muscle ache"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v10.get()=="Coughing"):
        if(l10.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l10.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l10.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

    if(v11.get()=="Sore throat"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set sore_throat=1 where sore_throat=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set sore_throat=2 where sore_throat=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set sore_throat=3 where sore_throat=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Fever"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set fever=1 where fever=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set fever=2 where fever=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set fever=3 where fever=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="swelling of body"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set swelling_of_body=1 where swelling_of_body=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set swelling_of_body=2 where swelling_of_body=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set swelling_of_body=3 where swelling_of_body=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Dizziness"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set dizziness=1 where dizziness=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set dizziness=2 where dizziness=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set dizziness=3 where dizziness=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Head ache"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set headache=1 where headache=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set headache=2 where headache=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set headache=3 where headache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Body ache"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set bodyache=1 where bodyache=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set bodyache=2 where bodyache=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set bodyache=3 where bodyache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Rash"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set rash=1 where rash=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set rash=2 where rash=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set rash=3 where rash=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Fatigue"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set fatigue=1 where fatigue=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set fatigue=2 where fatigue=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set fatigue=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Chills"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set chills=1 where fatigue=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set chills=2 where fatigue=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set chills=3 where fatigue=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Muscle ache"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set muscleache=1 where muscleache=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set muscleache=2 where muscleache=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set muscleache=3 where muscleache=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    elif(v11.get()=="Coughing"):
        if(l11.get()=="low"):
            cursor.execute("update symptoms set coughing=1 where coughing=0")
            conn.commit()
        elif(l11.get()=="mild"):
            cursor.execute("update symptoms set coughing=2 where coughing=0")
            conn.commit()
        elif(l11.get()=="high"):
            cursor.execute("update symptoms set coughing=3 where coughing=0")
            conn.commit()
        else:
            tkMessageBox.showinfo("Alert","Please insert low,mild or high")
    else:
        print ("not inserted")

root=Tk()
root.title("Symptoms")
root.configure(bg="aqua")
root.geometry("1000x700+200+0")
root.resizable(width=False,height=False)

v1 = StringVar()
v1.set("None")
v2 = StringVar()
v2.set("None")
v3 = StringVar()
v3.set("None")
v4 = StringVar()
v4.set("None")
v5 = StringVar()
v5.set("None")
v6 = StringVar()
v6.set("None")
v7 = StringVar()
v7.set("None")
v8 = StringVar()
v8.set("None")
v9 = StringVar()
v9.set("None")
v10 = StringVar()
v10.set("None")
v11= StringVar()
v11.set("None")

l1=StringVar()
l1.set("NULL")
l2=StringVar()
l2.set("NULL")
l3=StringVar()
l3.set("NULL")
l4=StringVar()
l4.set("NULL")
l5=StringVar()
l5.set("NULL")
l6=StringVar()
l6.set("NULL")
l7=StringVar()
l7.set("NULL")
l8=StringVar()
l8.set("NULL")
l9=StringVar()
l9.set("NULL")
l10=StringVar()
l10.set("NULL")
l11=StringVar()
l11.set("NULL")
res1=StringVar()

load=Image.open("pre.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

load1=Image.open("download.png")
render1=ImageTk.PhotoImage(load1)
img1=Label(root,image=render1)
img1.place(x=10,y=10)

ll1=Label(root,text="ENTER YOUR SYMPTOMS",bg="SteelBlue1",font=("times new roman",20,"bold"))
ll1.place(x=130,y=100)


w1 = ttk.Combobox(root, textvariable=v1,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w1.place(x=150,y=150)
o1=OptionMenu(root,l1,'low','mild','high')
o1.place(x=400,y=150)


w2 = ttk.Combobox(root, textvariable=v2,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w2.place(x=150,y=200)
o2=OptionMenu(root,l2,'low','mild','high')
o2.place(x=400,y=200)


w3 = ttk.Combobox(root, textvariable=v3,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w3.place(x=150,y=250)
o3=OptionMenu(root,l3,'low','mild','high')
o3.place(x=400,y=250)


w4 = ttk.Combobox(root, textvariable=v4,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w4.place(x=150,y=300)
o4=OptionMenu(root,l4,'low','mild','high')
o4.place(x=400,y=300)


w5 = ttk.Combobox(root, textvariable=v5,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w5.place(x=150,y=350)
o5=OptionMenu(root,l5,'low','mild','high')
o5.place(x=400,y=350)


w6 = ttk.Combobox(root, textvariable=v6,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w6.place(x=150,y=400)
o6=OptionMenu(root,l6,'low','mild','high')
o6.place(x=400,y=400)


w7 = ttk.Combobox(root, textvariable=v7,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w7.place(x=150,y=450)
o7=OptionMenu(root,l7,'low','mild','high')
o7.place(x=400,y=450)


w8 = ttk.Combobox(root, textvariable=v8,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w8.place(x=150,y=500)
o8=OptionMenu(root,l8,'low','mild','high')
o8.place(x=400,y=500)


w9 =ttk.Combobox(root, textvariable=v9,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w9.place(x=150,y=550)
o9=OptionMenu(root,l9,'low','mild','high')
o9.place(x=400,y=550)


w10 = ttk.Combobox(root, textvariable=v10,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w10.place(x=150,y=600)
o10=OptionMenu(root,l10,'low','mild','high')
o10.place(x=400,y=600)


w11= ttk.Combobox(root, textvariable=v11,values=["Sore throat", "Fever",'swelling of body',
                'Dizziness','Head ache','Body ache','Rash','Fatigue','Chills','Muscle ache','Coughing'],font=("times new roman",12))
w11.place(x=150,y=650)
o11=OptionMenu(root,l11,'low','mild','high')
o11.place(x=400,y=650)


b1=Button(root,command=symptoms,text="Upload Symptoms",bd=5,font=("times new roman",15),relief="solid",borderwidth=4)
b1.place(x=650,y=300)

b2=Button(root,command=upload,text="Click to start the diagnosis",bd=5,font=("times new roman",15),relief="solid",borderwidth=4)
b2.place(x=650,y=500)

e1=Entry(root,textvariable=res1,bg="SteelBlue1",fg="white",font=("times new roman",20,'bold','italic'),width=35)
e1.place(x=500,y=400)

root.mainloop()
