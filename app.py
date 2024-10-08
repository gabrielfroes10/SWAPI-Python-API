from flask import Flask, jsonify, request
import requests
from models import db, Character, Movie, Starship, Vehicle, Species, Planet, Favorite
from swapi_service import fetch_data
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def status():
    return jsonify({'status': 'OK'}), 200


@app.route('/characters', methods=['GET'])
def get_characters():
    characters = fetch_data('people/')
    return jsonify(characters), 200

@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = fetch_data(f'people/{id}/')
    if character:
        return jsonify(character), 200
    return jsonify({'error': 'Personagem não encontrado'}), 404

@app.route('/characters/<int:id>/save', methods=['POST'])
def save_character(id):
    character = fetch_data(f'people/{id}/')
    if character:
        new_char = Character(name=character['name'], birth_year=character['birth_year'])
        db.session.add(new_char)
        db.session.commit()
        return jsonify({'message': 'Personagem salvo com sucesso!'}), 201
    return jsonify({'error': 'Personagem não encontrado'}), 404

@app.route('/characters/<int:id>/delete', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if character:
        db.session.delete(character)
        db.session.commit()
        return jsonify({'message': 'Personagem deletado com sucesso!'}), 200
    return jsonify({'error': 'Personagem não encontrado'}), 404


@app.route('/movies', methods=['GET'])
def get_movies():
    movies = fetch_data('films/')
    return jsonify(movies), 200

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = fetch_data(f'films/{id}/')
    if movie:
        return jsonify(movie), 200
    return jsonify({'error': 'Filme não encontrado'}), 404

@app.route('/movies/<int:id>/save', methods=['POST'])
def save_movie(id):
    movie = fetch_data(f'films/{id}/')
    if movie:
        new_movie = Movie(title=movie['title'], episode_id=movie['episode_id'])
        db.session.add(new_movie)
        db.session.commit()
        return jsonify({'message': 'Filme salvo com sucesso!'}), 201
    return jsonify({'error': 'Filme não encontrado'}), 404

@app.route('/movies/<int:id>/delete', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Filme deletado com sucesso!'}), 200
    return jsonify({'error': 'Filme não encontrado'}), 404


@app.route('/favorito/save', methods=['POST'])
def save_favorite():
    data = request.get_json()
    favorite = Favorite(
        character_name=data['character_name'],
        movie_title=data['movie_title'],
        starship_name=data['starship_name'],
        vehicle_name=data['vehicle_name'],
        species_name=data['species_name'],
        planet_name=data['planet_name'],
    )
    db.session.add(favorite)
    db.session.commit()
    return jsonify({'message': 'Favorito salvo com sucesso!'}), 201

@app.route('/getFavorito', methods=['GET'])
def get_favorite():
    favorite = Favorite.query.first()
    if favorite:
        return jsonify({
            'Nome do personagem': favorite.character_name,
            'Nome do filme': favorite.movie_title,
            'Nome da nave': favorite.starship_name,
            'Nome do veículo': favorite.vehicle_name,
            'Nome da espécie': favorite.species_name,
            'Nome do planeta': favorite.planet_name,
        }), 200
    return jsonify({'error': 'Nenhum favorito encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
