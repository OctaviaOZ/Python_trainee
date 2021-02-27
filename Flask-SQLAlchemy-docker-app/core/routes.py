from flask import Flask, request
from flask import current_app as app

from controllers.actor import *
from controllers.movie import *


@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()


@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all get_all_movies in db
    """
    return get_all_movies()


@app.route('/api/actor', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():

    if request.method == 'POST':
        return add_actor()
    elif request.method == 'PUT':
        return update_actor()
    elif request.method == 'DELETE':
        return delete_actor()
    else:
        # Get  actor by id
        return get_actor_by_id()


@app.route('/api/movie', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():

    if request.method == 'POST':
        return add_movie()
    elif request.method == 'PUT':
        return update_movie()
    elif request.method == 'DELETE':
        return delete_movie()
    else:
        # Get  actor by id
        return get_movie_by_id()


@app.route('/api/actor-relations', methods=['PUT', 'DELETE'])
@app.route('/api/actor_relations', methods=['PUT', 'DELETE'])
def actor_relations():

    if request.method == 'DELETE':
        return actor_clear_relations()
    else:
        print('PUT')
        return actor_add_relation()

@app.route('/api/movie-relations', methods=['PUT', 'DELETE'])
@app.route('/api/movie_relations', methods=['PUT', 'DELETE'])
def movie_relations():

    if request.method == 'DELETE':
        return movie_clear_relations()
    else:
        return movie_add_relation()