from functools import wraps
from flask import session, jsonify
from app.storage.data import load_data
from config import BASEDIR
from hashlib import sha224
from subprocess import Popen, PIPE


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


def create_uniqid(command):
    uniqid = None
    DATA = load_data()
    data = DATA['scripts'];
    for k in data:
        if cmd in k.keys():
            p = ['processName']
            uniqid = sha224(p.encode('utf-8')).hexdigest()

    return uniqid

def daemon_process(command, command_list):
    result = {'status': None, 'message': None}
    uniq_id = sha224(command.encode('utf-8')).hexdigest()
    cmd_list = ['python3', '%s/daemon.py' % BASEDIR, uniq_id, command]
    cmd_list += command_list
    print(cmd_list)
    try:
        p = Popen(cmd_list, shell=False, stdout=PIPE, stderr=PIPE)
        p.wait()
        (out, err) = p.communicate(timeout=3)
        if p.returncode == 0:
            result = {'status': 'OK'}
        else:
            result = {'status': 'ERROR',
                      'message': err.decode('utf8')}
    except Exception as e:
        result = {'status': 'ERROR',
                  'message': str(e)}
    return result