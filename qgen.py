import csv
import numpy as np
from random import *
x=[1,2,3,4,5,6,7,8,9,10]
mark=[10,20,30,40,50,60,70,80,90]
i=x.index(min(x))
if mark[i]>70:
	csvFile = open("questions/%02dh.csv"%i, "rb")
elif mark[i] >40:
	csvFile = open("questions/%02dm.csv" % i, "rb")
else:
	csvFile = open("questions/%02de.csv"%i, "rb")

csvReader = csv.reader(csvFile)
i=0
ques=[]
choice=[]
answer=[]
for row in csvReader:
	qn=row[0:1]
	optn=row[1:5]
	an=row[5:6]
	ques.append(qn)
	choice.append(optn)
	answer.append(an)
i=randint(0,ques.__len__()-1)
print ques[i]
print choice[i]
print answer[i]