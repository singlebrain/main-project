from datetime import timedelta
import csv
import os
import numpy as np
from keras.models import load_model
from random import *
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import models as dbHandler
app = Flask(__name__)
@app.route("/")
def home():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		 return redirect(url_for('questions'))#first page to display

@app.route("/login",methods=['POST', 'GET'])
def login():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		user = dbHandler.retrieveUsers()
		udic=dict( user)
		print udic
		if username not in udic.keys():
			flash('user not found!')
		elif password==udic[username]:
			session['logged_in'] = True
			session['username'] = username
		else:
			flash('wrong password!')
		return home()
   	else:
   		return render_template('index.html')
@app.route("/logout")
def logout():
	session.pop('logged_in',None)
	session.pop('username',None)
	return home()
'''
@app.route("/signup",methods=['POST', 'GET'])
def signup():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)
   		users = dbHandler.retrieveUsers()
		return render_template('index.html', users=users)
   	else:
   		return render_template('index.html')
'''
@app.route("/questions",methods=['POST', 'GET'])
def questions():
	model = load_model('model/my_model.h5')
	username=session.get('username')
	userdata=dbHandler.useralldetail(username)
	userdata=list(userdata[0])
	print userdata
	eff=userdata[3:23]
	print eff
	xtet=[]
	xtet.append(eff)
	print xtet
	#xtet=[[10,20,30,40,50,60,70,80,90,95,1,2,3,4,5,6,7,8,9,10]]
	ytr=model.predict_proba(np.array(xtet))
	ytr=ytr.tolist()
	print ytr
	ytr=ytr[0]
	mark=[10,20,30,40,50,60,70,80,90]
	i=ytr.index(max(ytr))
	print i
	session['subject']=i
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
	data.append( ques[i])
	data.append(  choice[i])
	data.append(  answer[i])
	session['answer']=data
	return render_template("questions.html" , data=data)
@app.route("/answercheck",methods=['POST', 'GET'])
def answercheck():
	choice = request.form['foo']
	data =  session.get('answer')
	print choice
	print data[2][0]
	i=session.get('subject')
	username=session.get('username')
	print username
	print i
	if choice==data[2][0]:
		rep=['your answer is correct']
		dbHandler.increasemark(i,username)
	else:
		rep = ['your answer is wrong']
		dbHandler.decreasemark(i,username)
	data.append(rep)
	data.append(choice)
	print data
	return render_template("response.html" , data=data,choice=choice)   
@app.route("/dashboard")
def dashb():
    return render_template("dashboard.html" , text="asd")
    
@app.route("/notes")
def notes():
    return render_template("notes.html" , text="asd")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html" , text="asd")
    
@app.route("/user")
def user():
    return render_template("user.html" , text="asd")

@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=30)

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(port=8001,debug = True)
