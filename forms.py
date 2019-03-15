from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class StoryForm(FlaskForm):
    """Form to input story information."""

    place = StringField('place', validators=[DataRequired()])
    noun = StringField('noun', validators=[DataRequired()])
    verb = StringField('verb', validators=[DataRequired()])
    adjective = StringField('adjective', validators=[DataRequired()])
    plural_noun = StringField('plural_noun', validators=[DataRequired()])