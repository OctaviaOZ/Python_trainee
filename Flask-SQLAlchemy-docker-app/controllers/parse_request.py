from flask import request


def get_request_data():
    """
    Get keys & values from request
    """
    keys = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(keys, values))

    return data