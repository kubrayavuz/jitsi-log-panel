import json
from config import DATA_PATH
from collections import OrderedDict


def load_data():
    with open(DATA_PATH) as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def set_password(current_user, password):
    data = load_data()
    data['users'][current_user]['password'] = password

    with open(DATA_PATH, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)


def get_password_hash(current_user):
    return load_data()['users'].get(current_user)['password']


data = load_data()