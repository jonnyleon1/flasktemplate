# run.py
import os
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'COMP30670' # Feel free to put your name here!
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)


if __name__ == "__main__":
 	app.run()