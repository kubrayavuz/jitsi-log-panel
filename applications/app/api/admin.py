from flask_restful import Api, Resource
from flask import Blueprint, request, session
from app.api.schema import (LOGIN_SCHEMA, PASSWORD_SCHEMA)
from app.storage.data import load_data, set_password, get_password_hash
from schema import SchemaError
from app.api.helpers import login_required
from hashlib import sha256

api_bp = Blueprint('admin_api', __name__)
api = Api(api_bp)

DATA = load_data()


class Auth(Resource):

    def post(self):
        try:
            data = LOGIN_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}
        user = DATA['users'].get(data['username'], None)
        if not user:
            result = {'status': 'ERROR',
                      'message': 'Unauthorized user'}
        elif (get_password_hash(data['username']) !=
                sha256(data['password'].encode('utf8')).hexdigest()):
            result = {'status': 'Error',
                      'message': 'Unauthorized user'}
        else:
            session['username'] = data['username']
            result = {'status': 'OK',
                      'data': {'username': data['username']}}
        return result


    @login_required
    def put(self):
        try:
            data = PASSWORD_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'ERROR',
                    'message': e.code}
        if (get_password_hash(session['username']) !=
            sha256(data['old_password'].encode('utf8')).hexdigest()):
            result = {'status': 'ERROR',
                      'message': 'Unauthorized user'}

        elif len(data['password']) < 8:
            result = {'status': 'ERROR',
                      'message': 'Password must be at least 8 characters'}

        else:
            set_password(session['username'],
                         sha256(data['password'].encode('utf8')).hexdigest())
            del session['username']
            result = {'status': 'OK'}

        return result


    def delete(self):
        username = session.get('username', None)
        if username is not None:
            del session['username']
        return {'status': 'OK'}


api.add_resource(Auth, '/api/auth')
