from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template("home/index.html")



@app.route('/segunda')
def segunda():
    return render_template("login/index.html")