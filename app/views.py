from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adios')
def second_page():
    return render_template('adios.html')

