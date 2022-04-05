from crypt import methods
from flask import Flask, get_flashed_messages, url_for, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/', methods=["GET"])
def home_page():


    
    return redirect('/new_pet')

@app.route('/new_pet', methods=["GET", "POST"])
def show_pet_form():

    form = AddPetForm()

    if form.validate_on_submit():
        

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available
            
        )
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}")
        
       
        return redirect(f"/adopt/{new_pet.id}")

    else:
        return render_template(
            "new_pet.html", form=form)

@app.route('/adopt', methods=["GET"])
def show_pets():

    pets = Pet.query.all()

    return render_template('adopt.html', pets=pets)

@app.route('/adopt/<int:pet_id>', methods=["GET", "POST"])
def show_pet_profile(pet_id):

    msgs = get_flashed_messages()

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(object=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return render_template('pet_profile.html', pet=pet, form=form)

    else:
        flash("Edit failed")
        return render_template('pet_profile.html', pet=pet, form=form, msgs=msgs)

# @app.route('/adopt/<int:pet_id>/edit', methods=["GET", "POST"])
# def edit_pet(pet_id):

#     msgs = get_flashed_messages()

#     pet = Pet.query.get_or_404(pet_id)








