from flask import jsonify, make_response

from datetime import datetime as dt
from ast import literal_eval

from models.movie import Movie
from models.actor import Actor
from settings.constants import ACTOR_FIELDS, DATE_FORMAT  # to make response pretty
from .parse_request import get_request_data


def get_all_actors():
    """
    Get list of all records
    """
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        actors.append(act)
    return make_response(jsonify(actors), 200)


def get_actor_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_actor():
    """
    Add new actor
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    keys = data.keys()
    actors_attr = ['name', 'gender', 'date_of_birth']

    # for only included in list without redunant fields
    allTrue = [key in actors_attr for key in keys]
    if len(keys) == sum(allTrue):

        try:
            name = str(data['name'])
        except:
            err = 'Not found string Name. Adding failed'
            return make_response(jsonify(error=err), 400)

        if not name:
            err = 'Name should not be empty. Adding failed'
            return make_response(jsonify(error=err), 400)

        if 'date_of_birth' in keys:
            try:
                dt.strptime(data['date_of_birth'], DATE_FORMAT).date()
            except:
                err = f'Date_of_birth must be in format {DATE_FORMAT}'
                return make_response(jsonify(error=err), 400)

    else:
        err = f'Required fields: {actors_attr}. Got {keys}. Adding failed'
        return make_response(jsonify(error=err), 400)


    new_record = Actor.create(**data)
    new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
    return make_response(jsonify(new_actor), 200)
    ### END CODE HERE ###


def update_actor():
    """
    Update actor record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    keys = data.keys()

    allTrue = [key in ACTOR_FIELDS for key in keys]
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

        if 'date_of_birth' in keys:
            try:
                dt.strptime(data['date_of_birth'], DATE_FORMAT).date()
            except:
                err = f'Date_of_birth must be in format {DATE_FORMAT}. Updating failed'
                return make_response(jsonify(error=err), 400)

    else:
        err = f'Required fields: {ACTOR_FIELDS}. Got {keys}. Updating failed'
        return make_response(jsonify(error=err), 400)

    upd_record = Actor.update(row_id, **data)
    if upd_record:
        # use this for 200 response code
        upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in ACTOR_FIELDS}
        return make_response(jsonify(upd_actor), 200)
    else:
        err = f'Could not get record wih id {row_id}. Updating failed'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def delete_actor():
    """
    Delete actor by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
    except:
        err = 'Not found integer Id. Deleting failed'
        return make_response(jsonify(error=err), 400)

    if Actor.delete(row_id):
        # use this for 200 response code
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)
    else:
        err = f'Could not get record wih id {row_id} or it has links. Deleting failed'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###


def actor_add_relation():
    """
    Add a movie to actor's filmography
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
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
    actor = Actor.query.filter_by(id=row_id).first()
    movie = Movie.query.filter_by(id=rel_id).first()
    if not actor:
        err = f'Could not find record wih id {row_id}. Adding relation failed'
        return make_response(jsonify(error=err), 400)
    elif not movie:
        err = f'Could not find record wih relation_id {rel_id}. Adding relation failed'
        return make_response(jsonify(error=err), 400)
    else:
        Actor.add_relation(row_id, movie)
        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['filmography'] = str(actor.filmography)
        return make_response(jsonify(rel_actor), 200)
    ### END CODE HERE ###


def actor_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Not found integer Id. Clearing relations failed'
            return make_response(jsonify(error=err), 400)

        # use this for 200 response code
        actor = Actor.query.filter_by(id=row_id).first()
        if not actor:
            err = f'Could not get record wih id {row_id}. Clearing relations failed'
            return make_response(jsonify(error=err), 400)
        else:
            Actor.clear_relations(row_id)# clear relations here
            rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
            rel_actor['filmography'] = str(actor.filmography)
            return make_response(jsonify(rel_actor), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###