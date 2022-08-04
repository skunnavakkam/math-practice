
from flask import Flask, render_template
import sqlite3
import random
import pyrebase

## FIREBASE STUFF ##
config = {
    "apiKey": "AIzaSyDpcvFe3H4uYwyHHwz1WEdP5GxWYUFCXPo",
    "authDomain": "math-practice-6b4cb.firebaseapp.com",
    "projectId": "math-practice-6b4cb",
    "storageBucket": "math-practice-6b4cb.appspot.com",
    "messagingSenderId": "626197126343",
    "appId": "1:626197126343:web:3c8f36ca9373083c1f72e2",
    "measurementId": "G-5FD202CJ27"
}

firebase = pyrebase.initialize_app(config)  
auth = firebase.auth()

app = Flask(__name__)

# home, the pretty shit
@app.route("/")
def home():
    return render_template("home.html")

# overarching topics page
@app.route("/topics")
def topics():
    return render_template("topics.html")

# a way to navigate within topics
@app.route("/topic-overview/<topic>")
def topic_overview(topic):
    
    con = sqlite3.connect("problems.db")
    cur = con.cursor()
    
    temp = cur.execute("SELECT * FROM topics WHERE topic=:topic", {"topic": topic}).fetchall()
    problems = [[i[1], i[2]] for i in temp]
    return render_template("topic-overview.html", topic=topic.title(), problems=problems)

# gives you the problem
@app.route("/problems/<name>")
def problems(name):
    
    con = sqlite3.connect("problems.db")
    cur = con.cursor()
    
    temp = cur.execute("SELECT * FROM problems WHERE name=:name", {"name": name}).fetchall()
    
    if not len(temp):
        return "<h1>Not found<h1> <a href='/'>home</a>"
    
    problem = random.choice(temp)
    data = get_data(problem[2])
    
    if type(data['answer']) == list:
        return render_template('multiple-choice.html', question=data['question'], answer=data['answer'], is_calc=data['is_calc'])
    else: 
        return render_template('text-question.html', question=data['question'], answer=data['answer'], is_calc=data['is_calc'])
    
    
########################################
####        HELPER FUNCTIONS        ####
########################################
def get_data(code):
    loc = {}
    exec(code, globals(), loc)
    return loc['data']
