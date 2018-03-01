from datetime import timedelta
import datetime
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
		 return redirect(url_for('dashboard'))#first page to display

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
   		return render_template('login.html')
@app.route("/logout")
def logout():
	session.pop('logged_in',None)
	session.pop('username',None)
	return home()
@app.route("/signup",methods=['POST', 'GET'])
def signup():
	if request.method=='POST':
		print "qwertyuio1\n"
   		username = request.form['username']
		print "zxcvbnm"
   		email = request.form['email']
   		password = request.form['password']
   		dbHandler.insertUser(username, password,email)
   		#users = dbHandler.retrieveUsers()
		return redirect(url_for('home'))
		#return render_template('register.html')
   	else:
   		return render_template('register.html')
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
	#mark=[10,20,30,40,50,60,70,80,90]
	mark=userdata[3:13]
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
	j=0
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
	j=randint(0,ques.__len__()-1)
	data.append( ques[j])
	data.append(  choice[j])
	data.append(  answer[j])
	session['answer']=data
	label = ["oper sym","Comp Net","theory comp.","comp arch","compiler","maths","data struc","Algorithm","digital elect","DBMs"]
	return render_template("questions.html" , data=data,username=username,i=i,label=label)
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
	label = ["oper sym","Comp Net","theory comp.","comp arch","compiler","maths","data struc","Algorithm","digital elect","DBMs"]
	return render_template("response.html" , data=data,choice=choice,i=i,label=label)   
@app.route("/dashboard")
def dashboard():
	username=session.get('username')
	now = datetime.datetime.now()
	uslog=dbHandler.logindetail(username)
	uslog=list(uslog[0])
	print uslog
	print now.year
	print now.month
	cur=now.year*100+now.month
	data=dbHandler.useralldetail(username)
	data=list(data[0])
	
	labels = ["oper sym","Comp Net","theory comp.","comp arch","compiler","maths","data struc","Algorithm","digital elect","DBMs"]
	values = data[3:13] #[10,9,8,7,6,4,7,8,6,7]
	if not cur==uslog[1]:
		dbHandler.insertlife(username,cur,values)
	lifedata=dbHandler.retrievelife(username)
	lifelabel=[]
	lifevalue=[]
	print lifedata
	for life in lifedata:
		life=list(life)
		lifelabel.append(life[1])
		life=life[2:12]
		lifevalue.append(life)
	print lifelabel
	print lifevalue
	lifedat=list(lifedata)
	return render_template("dashboard.html" , values=values, labels=labels,username=username,lifelabel=lifelabel, lifevalue=lifevalue)
 
@app.route("/notes")
def notes():
    username=session.get('username')
    return render_template("notes.html" ,username=username)

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html" , text="asd")
    
@app.route("/user",methods=['POST', 'GET'])
def user():
	username=session.get('username')
	if request.method=='POST':
		print "post"
		email = request.form['email']
		print "post3"
		phone = request.form['phone']
		print "post2"
   		password = request.form['password']
		username=session.get('username')
		print "post1"
		dbHandler.updateuser(username,password,email,phone)
		return redirect(url_for('dashboard'))
	else:
		return render_template("user.html" , username=username)

@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=30)

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(port=8001,debug = True)
