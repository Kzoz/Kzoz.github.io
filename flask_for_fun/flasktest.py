#export FLASK_APP=flasktest
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return '<p> Hello, World! </p>'
