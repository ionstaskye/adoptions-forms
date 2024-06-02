from flask import Flask, render_template, redirect, request
from adopt_models import db, connect_db, Pet , AddPetForm
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)
with app.app_context():db.create_all()

@app.route('/')
def display_home():
    pets = Pet.query.all()

    return render_template("base.html", pets = pets)

@app.route("/add", methods= ["GET", "POST"])
def add_pet_form():

    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data  
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name= name, species= species, photo_url=photo_url, age= age, notes= notes)
        db.session.add(pet)
        db.session.commit()
        return redirect (f"/{pet.id}")
    else:
        return render_template("add_pet_form.html", form = form)

@app.route("/<int:pet_id>", methods = ["GET", "POST"])
def display_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj =pet)

    if form.validate_on_submit:
        name = form.name.data  
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name= name, species= species, photo_url=photo_url, age= age, notes= notes)
        db.session.add(pet)
        db.session.commit()
        return redirect (f"/{pet.id}")

    else:
        return render_template("pet_info.html", pet = pet, form = form)