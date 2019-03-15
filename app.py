from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
from forms import StoryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def render_form():
    """Render questions for madlibs form"""

    form = StoryForm()

    if form.validate_on_submit():
        place = form.place.data
        noun = form.noun.data
        verb = form.verb.data
        adjective = form.adjective.data
        plural_noun = form. plural_noun.data
        return f"These are the things in the form: {place}, {noun}, {verb}, {adjective}, {plural_noun}"
    else:
        return render_template("questions_form.html", form=form)

# @app.route('/story')
# def render_story():