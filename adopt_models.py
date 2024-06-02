

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

db= SQLAlchemy()

class Pet(db.Model):

    __tablename__ = "pets"


    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)
    name = db.Column(db.String(15),
                    nullable = False)
    species = db.Column(db.String(15),
                    nullable = False)
    photo_url = db.Column(db.String(),
                    )
    age = db.Column(db.Integer)

    notes = db.Column(db.String())

    available = db.Column(db.Boolean, default = True, nullable = False)

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators =[InputRequired(message = "Please input a name")])
    species = StringField("Species", validators = [InputRequired(message = "Please input a species"),  AnyOf(["dog","cat","porcupine"])])
    photo_url = StringField("Photo URL", validators = [Optional(), URL(message = "Please input valid URL")])
    age = FloatField("Age", validators = [Optional(), NumberRange(min = 0, max = 30, message = "Please input age 0-30")])
    notes = StringField("Notes", validators =  [Optional()])

class EditPetForm(FlaskForm):
    
    photo_url = StringField("Photo URL", Optional(), URL(message = "Please input valid URL"))
    notes = StringField("Notes", Optional())
    avaliable = BooleanField("Available")


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)