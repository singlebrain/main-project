import csv
import numpy as np
from keras.models import Sequential
from keras.models import Model
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
# Generate dummy data
x_train = np.random.random((10, 20))
y_train = np.random.randint(2, size=(10, 10))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 10))

model = Sequential()
model.add(Dense(512, input_dim=20, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
'''
model.add(Dense(20, input_dim=5, init='uniform', activation='tanh'))
model.add(Dense(1, init='uniform', activation='linear'))

# Compile model
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X1, Y1, nb_epoch=5000, batch_size=10,  verbose=2)
numpy.savetxt("trainresults.csv", PredTestSet, delimiter=",")
numpy.savetxt("valresults.csv", PredValSet, delimiter=",")
'''
x_tra = []
y_tra=[]
xtr=[]
ytr=[]
csvFile = open("sp.csv", "rb")
csvReader = csv.reader(csvFile)
i=0
for row in csvReader:
	x_tra=row[0:20]
	y_tra=row[20:30]
	xtr.append(x_tra)
	ytr.append(y_tra)
x=[10,20,30,40,50,60,70,80,90,100,1,2,3,4,5,6,7,8,9,10]
model.fit(xtr, ytr,epochs=20,batch_size=1)
score = model.evaluate(x_test, y_test, batch_size=128)
xtet=[]
xtet.append(x)
ytr=model.predict_proba(np.array(xtet))
print ytr

