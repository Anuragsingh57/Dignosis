import pandas
import csv
import csv
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import mysql.connector
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
print lr.fit(trainingX,trainingY)

print lr.predict([testingX[1]])

