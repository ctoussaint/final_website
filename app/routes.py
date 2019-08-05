import os
from app import app
from flask import render_template, request, redirect, url_for, session




from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'final_database' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:solarsystem(9)@cluster0-kczhr.mongodb.net/final_database?retryWrites=true&w=majority' 

mongo = PyMongo(app)
app.secret_key = b'2]\xc0\x9e\x96y\x193+\x0c\x1c\x035\xc0\xb8t'

# INDEX

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""


@app.route('/signup', methods=["GET", "POST"])
    

def signup():
    if request.method == "POST":
        # take in the info they gave us, check if username is taken, if username is available put into a database of users
        users = mongo.db.users
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user is None:
            users.insert({"username":request.form['username'],"password":request.form['password']})
            return redirect(url_for("scheduling"))
        else:
            return "That username is taken. Try logging in, or try a different usename"
        
    else:
        return render_template("signup.html")
        
        
        

@app.route('/login', methods=["GET","POST"])

def login():
    if request.method == "POST":
        users = mongo.db.users
    # use the username to find the account
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user:
        # check if the password is right
            if existing_user['password'] == request.form['password'] :
                session['username'] = request.form['username']
                return redirect(url_for('scheduling'))
            else:
                return "Your password doesn't match your username."
        else:
            return "There is no user with that username. Try making an account."
    else: 
         return render_template("login.html")
         
         

@app.route('/logout')

def logout():
    session.clear()
    return redirect('/')
    
    
    
@app.route('/scheduling', methods=['GET','POST'])

def scheduling():
    if request.method == "POST":
       return "You made an account"
    
    else:
        return render_template("scheduling.html")
        
        
        
        
@app.route('/about-us')

def about_us():
        return render_template("about-us.html")
        
        
        
        
@app.route('/finalpage')

def finalpage():
     return render_template("finalpage.html")
   
    
    
    
    
@app.route('/attractions')

def attractions():
    return render_template("attractions.html")

        
    
       

