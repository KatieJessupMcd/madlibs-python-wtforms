from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
from forms import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def render_form(): 

@app.route('/story')
def render_story():
    