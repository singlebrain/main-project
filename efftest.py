import csv
import numpy as np
from keras.models import load_model
from random import *
model = load_model('model/my_model.h5')
csvFile = open("testdata.csv", "rb")
csvReader = csv.reader(csvFile)
count=0
c=0
co=0
cw=0
for row in csvReader:
    x_tra = []
    x_tra.append(row[0:20])
    y_tra = row[20:30]
    ytr=model.predict_proba(np.array(x_tra))
    ytr=ytr.tolist()
    ytr=ytr[0]
    i=ytr.index(max(ytr))
    j=y_tra.index(max(y_tra))
    k=y_tra.index(min(y_tra))
    c=c+1
    if i==j:
        count=count+1
    else:
        print ytr
        print y_tra
        print i
        print j
        del y_tra[j]
        j = y_tra.index(max(y_tra))
        if i==j:
            co = co + 1
        if i==k:
            cw=cw+1
    print count*100.0/c
    print co*100.0/c
    print cw*100.0/c
