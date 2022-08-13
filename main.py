
from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

# home, the pretty shit
@app.route("/")
def home():
    return render_template("home.html")

# overarching topics age
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
        return render_template('question/multiple-choice.html', question=data['question'], answer=data['answer'], is_calc=data['is_calc'])
    else: 
        return render_template('question/text-question.html', question=data['question'], answer=data['answer'], is_calc=data['is_calc'])

@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/cumcumcumcum')
def cumcumcum():
    return render_template('question/question.html')

########################################
####        HELPER FUNCTIONS        ####
########################################
def get_data(code):
    loc = {}
    exec(code, globals(), loc)
    return loc['data']

