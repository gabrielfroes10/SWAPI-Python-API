from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birth_year = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    episode_id = db.Column(db.Integer)

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    model = db.Column(db.String(100))

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    model = db.Column(db.String(100))

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    language = db.Column(db.String(100))

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    population = db.Column(db.String(100))

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(100))
    movie_title = db.Column(db.String(100))
    starship_name = db.Column(db.String(100))
    vehicle_name = db.Column(db.String(100))
    species_name = db.Column(db.String(100))
    planet_name = db.Column(db.String(100))
