from functools import wraps
from flask import session, jsonify
from app.storage.data import load_data


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if session.get('username', None):
            return f(*args, **kwargs)
        else:
            response = jsonify(
                message = 'Unauthorized user, please re-login to system.',
                status = 401)
            return response

    return wrapped


def check_script(cmd):
    result = {'status': 'ERROR', 'path': None, 'message': ''}
    if cmd is not None:
        DATA = load_data()
        data = DATA['scripts'];
        for k in data:
            if cmd in k.keys():
                result = {'status': 'OK', 'path': k[cmd], 'message': None}
                break
            else:
                result['message'] = 'command not found'
    return result
