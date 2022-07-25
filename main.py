
from flask import Flask, render_template
import sqlite3
import random

def get_data(code):
    loc = {}
    exec(code, globals(), loc)
    return loc['data']

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/topics")
def topics():
    return render_template("topics.html")

@app.route("/topic-overview/<topic>")
def topic_overview(topic):
    
    con = sqlite3.connect("problems.db")
    cur = con.cursor()
    
    temp = cur.execute("SELECT * FROM topics WHERE topic=:topic", {"topic": topic}).fetchall()
    problems = [[i[1], i[2]] for i in temp]
    return render_template("topic-overview.html", topic=topic.title(), problems=problems)

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
        return render_template('multiple-choice.html', question=data['question'])
    else: return "i am bad at coding gimme a sec"
    
    
    