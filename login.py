from flask import Flask,render_template,request,redirect,url_for
import MySQLdb

app=Flask(__name__)
#conn=MySQLdb.connect(host="localhost",user="root",password="root",db="samostudium")
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////login.db
@app.route('/hello')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
	app.debug = True
#	app.run()	
	app.run(port=8000,debug = True)

'''def index():
	return render_template("index.html")'''
