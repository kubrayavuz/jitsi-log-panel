from flask_restful import Api, Resource
from flask import Blueprint, request
from app.api.helpers import (login_required, check_script)


api_bp = Blueprint('script_api', __name__)
api = Api(api_bp)


class Scripts(Resource):

    # @login_required
    def put(self):
        command = request.args.get('cmd', None)
        room = request.args.get('room', None)
        print(command)
        res = check_script(command)
        print(res)
        if command is None:
            return {'status': 'ERROR',
                    'message': 'Komut parametresi girilmeli'}


api.add_resource(Scripts, '/api/script')
