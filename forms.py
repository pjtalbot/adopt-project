from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Picture URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):

    
    photo_url = StringField("Picture URL")
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")
