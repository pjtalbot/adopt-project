from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL

class AddPetForm(FlaskForm):
    """Form for adding snacks."""
    select_species=[('cat', 'Cat'), ("dog", 'Dog'), ('porcupine', 'Porcupine')]

    name = StringField("Pet Name")
    species = SelectField("Species", choices=select_species, validators=[InputRequired()])
    photo_url = StringField("Picture URL", validators=[URL()])
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):

    
    photo_url = StringField("Picture URL", validators=[URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")
