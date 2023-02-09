from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from enum import Enum
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites= db.relationship('Favorites') 
    pets = db.relationship("Pet", backref="user")
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id,
            "email": self.email
            
            # do not serialize the password, its a security breach
        }
    def __repr__(self):
        return f'{self.name}'



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    race = db.Column(db.String(120), unique=False, nullable=False)
    castrated = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f'{self.name}'
    


class User_region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    contact_person_name = db.Column(db.String(100), unique=True, nullable=False)
    nif = db.Column(db.String(100), unique=True, nullable=False)
    contact_person_telf = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    country= db.Column(db.String(100), unique=True, nullable=False)
    city = db.Column(db.String(100), unique=True, nullable=False)
    regions = db.relationship('Region')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "contact_person_name": self.contact_person_name,
            "nif": self.nif,
            "contact_person_telf": self.contact_person_telf,
            "address": self.address,
            "country": self.country,
            "city": self.city

            # do not serialize the password, its a security breach
        }
    def __repr__(self):
        return f'{self.name}'

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    user_region = db.Column(db.Integer, db.ForeignKey('user_region.id'))
    restorations = db.relationship('Restoration' ,backref='region')
    accomodation = db.relationship('Accommodation', backref='region')
    experiences = db.relationship('Experience' ,backref='region')
    patrimonies = db.relationship('Patrimony' ,backref='region')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo

            # do not serialize the password, its a security breach
        }
    def __repr__(self):
        return f'{self.name}'

class RestorationChoices(Enum):
    bar= "bar"
    chiringuito= "chiringuito"
    restaurante= "restaurante"


class Restoration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    type_bussiness = db.Column(db.Enum(RestorationChoices), nullable=False, server_default="bar")
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            "type_bussiness": self.type_bussiness
            # do not serialize the password, its a security breach
        }

    def __repr__(self):
        return f'{self.name}'
class AccommodationChoices(Enum):
    hotel= "hotel"
    hostal= "hostal"
    albergue= "albergue"

class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    type_bussiness = db.Column(db.Enum(AccommodationChoices), nullable=False, server_default="hotel")
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            "type_bussiness": self.type_bussiness

            # do not serialize the password, its a security breach
        }
    def __repr__(self):
        return f'{self.name}'
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            
            # do not serialize the password, its a security breach
            }

    def __repr__(self):
        return f'{self.name}'

class Patrimony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),  nullable=False)
    resume = db.Column(db.Text, unique=False, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "resume": self.resume,
            "photo": self.photo,
            "logo": self.logo,
            
            # do not serialize the password, its a security breach
            }
    def __repr__(self):
        return f'{self.name}'
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    user= db.relationship('User')   
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship('Region')
    restoration_id = db.Column(db.Integer, db.ForeignKey('restoration.id'))
    restoration = db.relationship('Restoration')
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodation.id'))
    accommodation = db.relationship('Accommodation')
    patrimony_id = db.Column(db.Integer, db.ForeignKey('patrimony.id'))
    patrimony = db.relationship('Patrimony')

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user= db.relationship('User')
    user_region= db.relationship('User_region')
    user_region_id =db.Column(db.Integer, db.ForeignKey('user_region.id'))
    text = db.Column(db.Text, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship('Region')
    restoration_id = db.Column(db.Integer, db.ForeignKey('restoration.id'))
    restoration = db.relationship('Restoration')
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodation.id'))
    accommodation = db.relationship('Accommodation')
    patrimony_id = db.Column(db.Integer, db.ForeignKey('patrimony.id'))
    patrimony = db.relationship('Patrimony')
