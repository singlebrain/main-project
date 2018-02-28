import sqlite3 as sql
import datetime

def insertUser(username,password,email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
    con.commit()
    now = datetime.datetime.now()	
    current=now.year*100+now.month
    cur.execute("INSERT INTO logintime (username,lastin) VALUES (?,?)", (username,current))	
    con.commit()
    con.close()

def updateuser(username,password,email,phone):
	con = sql.connect("database.db")
	cur = con.cursor()
	print username
	print password
	print email
	print phone 
	cur.execute("UPDATE users SET password = \'"+str(password)+"\',email = \'"+str(email)+"\',phone = \'"+str(phone)+"\' WHERE username = \'"+str(username)+"\'")
	con.commit()
	con.close()

def insertlife(username,current,values):
	con = sql.connect("database.db")
	cur = con.cursor()
	values=[current]+values
	username=str(username)
	username.lstrip('u')
	values=[username]+values
	print tuple(values)
	cur.execute("INSERT INTO lifetime  VALUES "+str(tuple(values)))
	con.commit()
	cur.execute("UPDATE logintime SET lastin ="+str(current)+" WHERE username = \'"+username+"\'")
	con.commit()
	con.close()
def retrievelife(username):
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM lifetime WHERE username=\'"+username+"\' ORDER BY month")
	users = cur.fetchall()
	con.close()
	return users
def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users
def userdetail(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users WHERE username=%02s")%username
	user = cur.fetchall()
	con.close()
	return user

def useralldetail(username):
	con = sql.connect("database.db")
	cur = con.cursor()	
	cur.execute("SELECT * FROM users WHERE username=\'"+username+"\'")
	
	user = cur.fetchall()
	con.close()
	return user

def logindetail(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM logintime WHERE username=\'"+str(username)+"\'")
	user = cur.fetchall()
	con.close()
	return user

def increasemark(i,username):
	con = sql.connect("database.db")
	cur = con.cursor()
	#print username
	cur.execute("SELECT * FROM users WHERE username=\'"+username+"\'")
	user = cur.fetchall()
	#print user
	user=list(user[0])
	user[i+3]=(((user[i+3])/100.0*user[i+23]+1)*100)/(user[i+23]+1)
	user[i+23]=user[i+23]+1
	for j in range(10):
		if j==i:
			user[j+13]=1
		else:
			user[j+13]=user[j+13]+1
	us=str(user[1])
	pa=str(user[2])
	ph=str(user[33])
	em=str(user[34])
	us.lstrip('u')
	pa.lstrip('u')
	ph.lstrip('u')
	em.lstrip('u')
	user[1]=us
	user[2]=pa
	user[33]=ph
	user[34]=em
	#print user
	#print tuple(user)
	cur.execute("DELETE FROM users WHERE username =\'"+username+"\'")
	con.commit()
	cur.execute("INSERT INTO users  VALUES "+str(tuple(user)))
	con.commit()
	con.close()
def decreasemark(i,username):
	con = sql.connect("database.db")
	cur = con.cursor()
	#print username
	cur.execute("SELECT * FROM users WHERE username=\'"+username+"\'")
	user = cur.fetchall()
	#print user
	user=list(user[0])
	user[i+3]=(((user[i+3]/100.0)*user[i+23])*100)/(user[i+23]+1)
	user[i+23]=user[i+23]+1
	for j in range(10):
		if j==i:
			user[j+13]=1
		else:
			user[j+13]=user[j+13]+1
	us=str(user[1])
	pa=str(user[2])
	ph=str(user[33])
	em=str(user[34])
	us.lstrip('u')
	pa.lstrip('u')
	ph.lstrip('u')
	em.lstrip('u')
	user[1]=us
	user[2]=pa
	user[33]=ph
	user[34]=em
	#print user
	#print tuple(user)
	cur.execute("DELETE FROM users WHERE username =\'"+username+"\'")
	con.commit()
	cur.execute("INSERT INTO users  VALUES "+str(tuple(user)))
	con.commit()
	con.close()
