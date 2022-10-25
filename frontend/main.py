
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import requests


app = Flask(__name__)

@app.route("/", methods=['GET',])
def index():

    return render_template('index.html')
