from flask import jsonify, make_response

from ast import literal_eval

from models.movie import Movie
from models.actor import Actor
from settings.constants import MOVIE_FIELDS
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        act = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(act)
    return make_response(jsonify(movies), 200)

def get_movie_by_id():
    """
    Get record by id
    """
    data =  get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer. Getting failed'
            return make_response(jsonify(error=err), 400)

        obj = Movie.query.filter_by(id=row_id).first()
        try:
            movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
        except:
            err = 'Record with such id does not exist. Getting failed'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(movie), 200)

    else:
        err = 'No id specified. Getting failed'
        return make_response(jsonify(error=err), 400)


def add_movie():
    """
    Add new movie
    """
    data = get_request_data()
    # use this for 200 response code
    keys = data.keys()
    movies_attr = ['name', 'year', 'genre']

    # for only included in list without redunant fields
    allTrue = [key in movies_attr for key in keys]
    if len(keys) == sum(allTrue):

        try:
            name = str(data['name'])
        except:
            err = 'Not found string Name. Adding failed'
            return make_response(jsonify(error=err), 400)

        if not name:
            err = 'Name should not be empty. Adding failed'
            return make_response(jsonify(error=err), 400)

        if 'year' in keys:
            try:
                int(data['year'])
            except:
                err = 'Year must be integer. Adding failed'
                return make_response(jsonify(error=err), 400)

    else:
        err = f'Required fields: {movies_attr}. Got {keys}. Adding failed'
        return make_response(jsonify(error=err), 400)

    new_record = Movie.create(**data)
    new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
    return make_response(jsonify(new_movie), 200)


def update_movie():
    """
    Update movie record by id
    """
    data = get_request_data()
    keys = data.keys()

    # for only included in list without redunant fields
    allTrue = [key in MOVIE_FIELDS for key in keys]
    if len(keys) == sum(allTrue):

        try:
            row_id = int(data['id'])
        except:
            err = 'Not found integer Id. Updating failed'
            return make_response(jsonify(error=err), 400)

        try:
            name = str(data['name'])
        except:
            err = 'Not found string Name. Updating failed'
            return make_response(jsonify(error=err), 400)

        if not name:
            err = 'Name should not be empty. Updating failed'
            return make_response(jsonify(error=err), 400)

        if 'year' in keys:
            try:
                int(data['year'])
            except:
                err = 'Year must be integer. Updating failed'
                return make_response(jsonify(error=err), 400)

    else:
        err = f'Required fields: {MOVIE_FIELDS}. Got {keys}. Updating failed'
        return make_response(jsonify(error=err), 400)

    upd_record = Movie.update(row_id, **data)
    if upd_record:
        # use this for 200 response code
        upd_movie = {k: v for k, v in upd_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(upd_movie), 200)
    else:
        err = f'Could not get record wih id {row_id}. Updating failed'
        return make_response(jsonify(error=err), 400)



def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
    except:
        err = 'Not found integer Id. Deleting failed'
        return make_response(jsonify(error=err), 400)

    if Movie.delete(row_id):
        # use this for 200 response code
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)
    else:
        err = f'Could not get record wih id {row_id}. Deleting failed'
        return make_response(jsonify(error=err), 400)

def movie_add_relation():
    """
    Add actor to movie's cast
    """
    data = get_request_data()
    try:
        row_id = int(data['id'])
    except:
        err = 'Not found integer Id. Adding relation failed'
        return make_response(jsonify(error=err), 400)

    try:
        rel_id = int(data['relation_id'])
    except:
        err = 'Not found integer relation_id. Adding relation failed'
        return make_response(jsonify(error=err), 400)

    # use this for 200 response code
    # add relation here
    movie = Movie.query.filter_by(id=row_id).first()
    actor = Actor.query.filter_by(id=rel_id).first()
    if not actor:
        err = f'Could not find record wih relation_id {rel_id}. Adding relation failed'
        return make_response(jsonify(error=err), 400)
    elif not movie:
        err = f'Could not find record wih id {row_id}. Adding relation failed'
        return make_response(jsonify(error=err), 400)
    else:
        Movie.add_relation(row_id, actor)
        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['cast'] = str(movie.cast)
        return make_response(jsonify(rel_movie), 200)

def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Not found integer Id. Deleting relations failed'
            return make_response(jsonify(error=err), 400)

        # use this for 200 response code
        movie = Movie.query.filter_by(id=row_id).first()  # add relation here
        if not movie:
            err = f'Could not get record wih id {row_id}. Deleting relations failed'
            return make_response(jsonify(error=err), 400)
        else:
            Movie.clear_relations(row_id)# clear relations here
            rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['cast'] = str(movie.cast)
            return make_response(jsonify(rel_movie), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
