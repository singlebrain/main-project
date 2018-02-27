import csv
import numpy as np
from keras.models import load_model
from random import *
model = load_model('model/my_model.h5')
xtet=[[10,20,30,40,50,60,70,80,90,95,1,2,3,4,5,6,7,8,9,10]]
ytr=model.predict_proba(np.array(xtet))
ytr=ytr.tolist()
#print ytr

mark=[10,20,30,40,50,60,70,80,90]
i=ytr.index(max(ytr))
if mark[i]>75:
	csvFile = open("questions/%02dh.csv"%i, "rb")
elif mark[i] >40:
	csvFile = open("questions/%02dm.csv" %i, "rb")
else:
	csvFile = open("questions/%02de.csv"%i, "rb")

csvReader = csv.reader(csvFile)
i=0
ques=[]
choice=[]
answer=[]
data=[]
for row in csvReader:
	qn=row[0:1]
	optn=row[1:5]
	an=row[5:6]
	ques.append(qn)
	choice.append(optn)
	answer.append(an)
i=randint(0,ques.__len__()-1)
data.append(ques[i])
print choice[i]
print answer[i]
