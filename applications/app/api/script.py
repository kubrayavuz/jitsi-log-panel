from flask_restful import Api, Resource
from flask import Blueprint, request
from app.api.helpers import (login_required, check_script, daemon_process)
from config import SCRIPT_PATH

api_bp = Blueprint('script_api', __name__)
api = Api(api_bp)


class Scripts(Resource):

    # @login_required
    def put(self):
        res = {'status': 'ERROR', 'message': '', 'command_list': []}
        command = request.args.get('cmd', None)
        room = request.args.get('room', None)
        res = check_script(command)
        print(res)
        if command is None:
            return {'status': 'ERROR',
                    'message': 'Komut parametresi girilmeli'}
        script_path = SCRIPT_PATH + res['path']
        command_list = ['bash', script_path]
        res['command_list'] = command_list
        res = daemon_process(command, res['command_list'])
        print(res)

        return

api.add_resource(Scripts, '/api/script')
